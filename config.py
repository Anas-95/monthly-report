# Returns API headers of QRadar
def get_headers():
    return {
        'Version': '11.0',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'SEC': '1fdb30bf-ac3c-4563-95e9-f8e326095604'
    }


# Returns current directory
def get_dir():
    return os.path.dirname(__file__)


# Returns logs directory for current script
def get_logs_dir():
    return os.path.join(os.path.dirname(__file__), "logs")


