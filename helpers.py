# Takes start of the day time and a specific hour
# Returns the specified hour of a day
def hour_of_day(s_today, s_hour):
    s_time = s_today + timedelta(hours=s_hour)
    return s_time


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
                os.system(f'echo "Log: JSON File format not supported, {datetime.now().strftime("%b %dth, %Y %H:%M:%S")}" >> {Config.get_logs_dir()}/files.log')
                exit(0)
    except FileNotFoundError:
        os.system(f'echo "Log: File not found, {datetime.now().strftime("%b %dth, %Y %H:%M:%S")}" >> {Config.get_logs_dir()}/files.log')
        exit(0)