from os import path


# Returns API headers of QRadar
def get_headers():
    return {
        'Version': '11.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'SEC': '713e4a5b-e3f3-494f-982f-45edf327d0bc'
    }


# Returns current directory
def get_dir():
    return path.dirname(__file__)


# Returns logs directory for current script
def get_logs_dir():
    return path.join(path.dirname(__file__), "logs")


def json_files_dir():
    return "/home/scripts/offense-stat/exports/arc/"
