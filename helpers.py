import json
from json.decoder import JSONDecodeError
from os import system, path
from datetime import datetime
from config import get_dir, get_logs_dir
import pandas as pd


# Takes date
# Returns timestamp in milliseconds
def to_ms_timestamp(date_):
    ms_timestamp = datetime.timestamp(date_)
    return int(ms_timestamp * 1000)


# Read json file and returns the file
def read_json(file_path):
    try:
        with open(file_path) as f:
            try:
                return json.load(f)
            except JSONDecodeError:
                system(f'echo "Log: JSON File format not supported, {datetime.now().strftime("%b %dth, %Y %H:%M:%S")}" >> {get_logs_dir()}/files.log')
                exit(0)
    except FileNotFoundError:
        system(f'echo "Log: File not found, {datetime.now().strftime("%b %dth, %Y %H:%M:%S")}" >> {get_logs_dir()}/files.log')
        exit(0)


def write_to_file(logs_count, alerts_count, file_path):
    count = {
        "Logs Count": f"{logs_count:,}",
        "Alerts Count": f"{alerts_count:,}"
    }
    
    df = pd.DataFrame(count, index=[0])
    df.to_csv(file_path, index=False)
