import json
import requests
from time import sleep
from os import system, path
import urllib3
from datetime import datetime, timedelta
from config import get_headers, get_dir, get_logs_dir, json_files_dir
from helpers import to_ms_timestamp, read_json, write_to_file


if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.session()
    headers = get_headers()
    s_now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    s_current_year_week = s_now.strftime("%Y-%U")
    d_current_year_week = datetime.strptime(s_current_year_week+"-0", "%Y-%U-%w")
    d_year_last_4_weeks = []
    s_year_last_4_weeks = []

    for i in [0, 1, 2, 3]:
        d_year_last_4_weeks.append(d_current_year_week-timedelta(weeks=i))
    print(d_year_last_4_weeks)
    for d_yw in d_year_last_4_weeks:
        s_year_last_4_weeks.append(d_yw.strftime("%Y-%U"))
    print(s_year_last_4_weeks)
    logs_count = [read_json(f"{json_files_dir()}ec_{s_yw}.json")['Count'] for s_yw in s_year_last_4_weeks]
    
    logs_counts = 0
    for l in logs_count:
        for l_val in list(l.values()):
            if l_val:
                logs_counts += l_val
    logs_counts = int(logs_counts)

    #logs_count = int(sum([sum(l.values()) for l in logs_count]))
    
    timestamp_s_datetime = to_ms_timestamp(d_year_last_4_weeks[3])
    timestamp_e_datetime = to_ms_timestamp(d_current_year_week)

    filters = [f'start_time>={timestamp_s_datetime}', f'start_time<{timestamp_e_datetime}']
    fields = ['id']
    
    print(d_year_last_4_weeks[3], timestamp_s_datetime)
    print(d_current_year_week, timestamp_e_datetime)
    print(logs_counts)

    URL = f'https://ry1-core-siem.sic.sitco.sa/api/siem/offenses?fields={fields[0]}&filter={filters[0]} AND {filters[1]}' 
    resp = session.get(URL, headers=headers, verify=False)
    if resp.status_code == 200:
        resp = resp.json()
        if len(resp) > 0:
            alerts_count = len(resp)
            print(alerts_count)
            logs_alerts_path = path.abspath(path.join(get_dir(), "Logs_Alerts_Count.csv"))
            write_to_file(logs_counts, alerts_count, logs_alerts_path)
    else:
        print("Error: ", resp.status_code)
