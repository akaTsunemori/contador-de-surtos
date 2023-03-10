import discord
import json
import pytz
from datetime import datetime
from random import choice


from src.paginator import PaginatorView


gifs_file = open('gifs.json', 'r')
gifs = json.load(gifs_file)
gifs_keys = [i for i in gifs.keys()]
gifs_file.close()


def get_date(current_time: datetime = None) -> datetime:
    if not current_time:
        tz = pytz.timezone('America/Sao_Paulo')
        current_time = datetime.now(tz=tz)
    return current_time.strftime('%d/%m/%Y, %H:%M:%S')


def str_surto(date: str, reason: str):
    return f'**Surto:** {reason}\n**Data:** {date[:-3]}'


def save(id: int, surtos: dict, last_surtos: dict) -> None:
    surtos_db = open(f'./database/{id}.json', 'w')
    json.dump(surtos[id], surtos_db)
    surtos_db.close()
    last_surtos_db = open(f'./database/{id}_last.json', 'w')
    json.dump(last_surtos[id], last_surtos_db)
    last_surtos_db.close()


def get_gif(key: str = None) -> str:
    if not key:
        key = choice(gifs_keys)
    gif = choice(gifs[key])
    return gif


def surtos_view(surtos_from_id: list, color: int, title: str, description: str) -> PaginatorView:
    surtos_list = surtos_from_id.copy()
    surtos_list.reverse()
    embeds = []
    tmp_surtos_list = []
    surto_num = 1
    while surtos_list:
        date, reason = surtos_list.pop()
        surto_str = str_surto(date, reason)
        tmp_surtos_list.append(surto_str)
        if surtos_list and len(tmp_surtos_list) < 5:
            continue
        embed = discord.Embed(color=color)
        embed.title = title
        embed.description = description
        embed.set_image(url=get_gif())
        for surto in tmp_surtos_list:
            embed.add_field(name=f'{surto_num}.', value=surto, inline=False)
            surto_num += 1
        embeds.append(embed)
        tmp_surtos_list.clear()
    view = PaginatorView(embeds)
    return view