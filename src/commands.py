import datetime
import discord
from discord.ext import commands


import src.utils as utils
from src.bot_error import BotError


async def surto(context: commands.Context, surtos: dict, last_surtos: dict, *args) -> None:
    id = context.guild.id
    reason = ' '.join(args[0])
    if not reason:
        raise BotError('Nenhuma razão válida para o surto foi informada.')
    if len(reason) > 1900:
        raise BotError('Que surto grande é esse? Resume aí, por favor.')
    date = utils.get_date()
    surtos[id].append([date, reason])
    last_surtos[id] = [date, reason]
    utils.save(id, surtos, last_surtos)
    await context.channel.send(utils.str_surto(date, reason))


async def surtos(context: commands.Context, surtos: dict) -> None:
    id = context.guild.id
    if not surtos[id]:
        raise BotError('A lista de surtos está vazia.')
    surtos[id].sort(reverse=True)
    surtos_list = []
    chr_count = 0
    for date, reason in surtos[id]:
        surto_str = utils.str_surto(date, reason)
        if chr_count + len(surto_str) > 2000:
            chr_count = 0
            surtos_str = '\n\n'.join(surtos_list)
            await context.channel.send(surtos_str)
            surtos_list.clear()
        chr_count += len(surto_str)
        surtos_list.append(surto_str)
    if surtos_list:
        surtos_str = '\n\n'.join(surtos_list)
        await context.channel.send(surtos_str)



async def stats(id: int, channel: discord.TextChannel, surtos: dict, last_surtos: dict) -> None:
    if not surtos[id]:
        raise BotError('A lista de surtos está vazia.')
    amount = len(surtos[id])
    date, reason = last_surtos[id]
    ultimo_surto_datetime = datetime.datetime.strptime(date, '%d/%m/%Y, %H:%M')
    time_delta = datetime.datetime.now() - ultimo_surto_datetime
    await channel.send(
        f'Estamos há **{time_delta.days} dias** sem nenhum surto.\n'\
        f'No total, **{amount} surtos** foram registrados.\n\n'\
        f'O motivo do último surto foi **{reason}**,\n'\
        f'e aconteceu na data **{date}**.'
    )


async def reset(context: commands.Context, args: list, surtos: dict, last_surtos: dict) -> None:
    id = context.guild.id
    if not args:
        raise BotError('ID do servidor ausente.')
    if len(args) > 1:
        raise BotError('Argumento inválido: muitos argumentos informados.')
    try:
        input_id = int(args[0])
    except ValueError:
        raise BotError('Argumento inválido.')
    if input_id != id:
        raise BotError('O ID informado não corresponde ao ID do servidor.')
    surtos[id] = list()
    last_surtos[id] = list()
    utils.save(id, surtos, last_surtos)
    await context.channel.send('Feito.')

