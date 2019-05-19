import datetime as dt
from sqlite3 import connect


def timer(func):
    def wrapper(*args, **kwargs):
        start = dt.datetime.now()
        rv = func(*args, **kwargs)
        end = dt.datetime.now()
        log(str(func.__name__), start, end)
        return rv
    return wrapper


def log(func, start, end):
    with connect('database/logger') as conn:
        cur = conn.cursor()
        try:
            cur.execute('create table process_log(function text, process_start time, process_end time)')
        except Exception:
            pass

        cur.execute(f"insert into process_log values('{func}','{start}','{end}')")
