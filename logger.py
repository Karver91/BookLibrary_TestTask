import datetime

from config import settings


def log_exception(traceback):
    with open(settings.log_file_path, 'a') as file:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(timestamp, traceback, file=file)
