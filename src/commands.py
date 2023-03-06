import pytz
from datetime import datetime
from discord.ext import commands


import src.utils as utils
from src.bot_error import BotError


async def surto(context: commands.Context, surtos: dict, last_surtos: dict, *args) -> None:
    id = context.guild.id
    reason = ' '.join(args[0])
    if not reason:
        raise BotError('Nenhuma razão válida para o surto foi informada.')
    date = utils.get_date()
    surtos[id].append((date, reason))
    last_surtos[id] = (date, reason)
    utils.save(id, surtos, last_surtos)
    await context.channel.send(utils.str_surto(date, reason))


async def surtos(context: commands.Context, surtos: dict) -> None:
    id = context.guild.id
    surtos_list = []
    for date, reason in surtos[id]:
        surtos_list.append(utils.str_surto(date, reason))
    surtos_str = '\n\n'.join(surtos_list)
    if not surtos_str:
        raise BotError('A lista de surtos está vazia.')
    await context.channel.send(surtos_str)

