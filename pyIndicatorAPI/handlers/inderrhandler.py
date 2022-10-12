from datetime import datetime
import os


def handle_log(func):
    def wrapped(*args, **kwargs):
        msg = func(*args, **kwargs)
        date = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
        with open(f'{os.getcwd()}/logs.txt', 'a') as f:
            f.write(f'{date:7s} {msg}\n')
    return wrapped


@handle_log
def handle_status_code(response):
    status_code = response.status_code
    if status_code == 400:
        return "BAD REQUEST!"
    elif status_code == 401:
        return "UNAUTHORIZED! ENTER VALID API KEY!"
    elif status_code == 402:
        return "PAYMENT REQUIRED!"
    elif status_code == 403:
        return "FORBIDDEN! ENTER VALID API KEY!"
    elif status_code == 404:
        return "NOT FOUND!"
    elif status_code == 500:
        return "SERVER ERROR!"
    else:
        return "UNKNOWN ERROR!"
