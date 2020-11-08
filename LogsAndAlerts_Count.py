import json
import requests
from time import sleep
import pandas as pandas
from os import system, path
import urllib3
from json.decoder import JSONDecodeError
from datetime import timedelta
from datetime import datetime
from config import Config
from helpers import CustomTime, CustomFiles


if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    session = requests.session()
    headers = Config.get_headers()
    # logs_count = CustomFiles.read_json("/home/scripts/offense-stat/exports/arc/ec_2020-44.json")['Count']
    # logs_count = f"{int(sum(logs_count.values())):,}"
    today = datetime.today()
    s_time = hour_of_day(today_st, 1)
    e_time = hour_of_day(today_st, 1)
    timestamp_s_time = CustomTime.to_ms_timestamp(s_time)
    timestamp_e_time = CustomTime.to_ms_timestamp(e_time)
    print(today.strftime("%Y-%U"))
    exit(0)
    resp = session.get(f'https://ry1-core-siem.sic.sitco.sa/api/siem/offenses?fields=domain_id&filter=start_time>={timestamp_e_time} AND start_time<={timestamp_e_time}', headers=headers, verify=False)
    if resp.status_code == 200:
        resp = resp.json()
        resp2 = resp2.json()
        if len(resp) > 0 and len(resp2) > 0:
            write_offenses_to_file(session, resp, resp2, tenants)
            offenses_path = os.path.abspath(os.path.join(get_dir(),"Offenses_Count.csv"))
            os.system(f'echo "File attached" | mail -s "Offenses Count" -a {offenses_path} -c "aalmohsen@site.sa, ralharbi@site.sa" SOCL2@site.sa')
    else:
        print("Error: ", resp.status_code)
