import json
import requests
from time import sleep
import pandas as pandas
from os import system, path
import urllib3
from datetime import datetime, timedelta
from config import get_headers, get_dir, get_logs_dir, json_files_dir
from helpers import hour_of_day, to_ms_timestamp, read_json


if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    session = requests.session()
    headers = get_headers()
    today = datetime.today()
    current_year_week = today.strftime("%Y-%U")
    current_year = today.strftime("%Y")
    current_week = today.strftime("%U")
    weeks = reversed([eval(current_week + '-i') for i in range(1, 5)])
    logs_count = [read_json(f"{json_files_dir()}ec_{current_year}-{week}.json")['Count'] for week in weeks]
    logs_count = f"{int(sum([sum(l.values()) for l in logs_count])):,}"

    # print(datetime.now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)+timedelta(weeks=44))
    print(datetime.strptime(current_year_week, "%Y-%U"))
    delta_weeks = [today+timedelta(weeks=w) for w in weeks]
    # print([str(w) for w in delta_weeks], timedelta())
    # s_time = hour_of_day(today_st, 1)
    # e_time = hour_of_day(today_st, 1)
    # timestamp_s_time = to_ms_timestamp(s_time)
    # timestamp_e_time = to_ms_timestamp(e_time)
    # print(logs_count)
    exit(0)
    resp = session.get(f'https://ry1-core-siem.sic.sitco.sa/api/siem/offenses?fields=domain_id&filter=start_time>={timestamp_s_time} AND start_time<={timestamp_e_time}', headers=headers, verify=False)
    if resp.status_code == 200:
        resp = resp.json()
        if len(resp) > 0:
            # write_offenses_to_file(session, resp)
            offenses_path = path.abspath(path.join(get_dir(), "Offenses_Count.csv"))
    else:
        print("Error: ", resp.status_code)
