import pytz
from datetime import datetime


# https://docs.python.org/3/library/datetime.html#module-datetime
# I can just save the dates as objects and have a function to
# return them as strings, so I can easily calculate the time delta.


def get_date() -> str:
    tz = pytz.timezone('America/Sao_Paulo')
    current_time = datetime.now(tz=tz)
    return current_time.strftime('%d/%m/%Y, %H:%M')
