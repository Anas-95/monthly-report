import json
import requests
from time import sleep
import pandas as pandas
from os import system, path
import urllib3
from datetime import datetime, timedelta
from config import get_headers, get_dir, get_logs_dir, json_files_dir
from helpers import to_ms_timestamp, read_json


if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    session = requests.session()
    headers = get_headers()
    s_now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    s_current_year_week = s_now.strftime("%Y-%U")
    d_current_year_week = datetime.strptime(s_current_year_week+"-0", "%Y-%U-%w")
    s_current_year_week = s_current_year_week.split("-")
    d_year_last_4_weeks = []
    s_year_last_4_weeks = []

    for i in range(1, 5):
        d_year_last_4_weeks.append(d_current_year_week-timedelta(weeks=i))

    for d_yw in d_year_last_4_weeks:
        s_year_last_4_weeks.append(d_yw.strftime("%Y-%U"))

    # logs_count = [read_json(f"{json_files_dir()}ec_{s_yw}.json")['Count'] for s_yw in s_year_last_4_weeks]
    # logs_count = f"{int(sum([sum(l.values()) for l in logs_count])):,}"

    timestamp_s_datetime = to_ms_timestamp(datetime.timestamp(d_year_last_4_weeks[0]))
    timestamp_e_datetime = to_ms_timestamp(datetime.timestamp(d_current_year_week))
    print(timestamp_s_datetime)
    print(timestamp_e_datetime)
    exit(0)
    resp = session.get(f'''https://ry1-core-siem.sic.sitco.sa/api/siem/offenses?
                            fields=domain_id
                            &filter=start_time>={timestamp_s_datetime} AND start_time<{timestamp_e_datetime}''',
                       headers=headers, verify=False)
    if resp.status_code == 200:
        resp = resp.json()
        if len(resp) > 0:
            # write_offenses_to_file(session, resp)
            offenses_path = path.abspath(path.join(get_dir(), "Offenses_Count.csv"))
    else:
        print("Error: ", resp.status_code)
