import json
from json.decoder import JSONDecodeError
from os import system
from datetime import datetime
from config import get_logs_dir


# Takes timestamp in seconds
# Returns timestamp in milliseconds
def to_ms_timestamp(sec_timestamp):
    ms_timestamp = datetime.timestamp(sec_timestamp)
    ms_timestamp = int(ms_timestamp * 1000)
    return ms_timestamp


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