import json
import pytz
from datetime import datetime
from discord.ext import commands


# https://docs.python.org/3/library/datetime.html#module-datetime
# I can just save the dates as objects and have a function to
# return them as strings, so I can easily calculate the time delta.


def get_date() -> str:
    tz = pytz.timezone('America/Sao_Paulo')
    current_time = datetime.now(tz=tz)
    return current_time.strftime('%d/%m/%Y, %H:%M')


def save(context: commands.Context, surtos: dict, last_surtos: dict) -> None:
    id = context.guild.id
    surtos_db = open(f'./database/{id}.json', 'w')
    json.dump(surtos[id], surtos_db)
    surtos_db.close()
    last_surtos_db = open(f'./database/{id}_last.json', 'w')
    json.dump(last_surtos[id], last_surtos_db)
    last_surtos_db.close()

