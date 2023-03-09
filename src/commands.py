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
    if len(reason) > 900:
        raise BotError('Que surto grande é esse? Resume aí, por favor.')
    date = utils.get_date()
    surtos[id].append([date, reason])
    last_surtos[id] = [date, reason]
    utils.save(id, surtos, last_surtos)
    await context.channel.send(utils.str_surto(date, reason))


async def surtos(context: commands.Context, surtos: dict) -> None:
    id = context.guild.id
    surtos_from_id: list = surtos[id].copy()
    surtos_from_id.sort(reverse=True)
    view = utils.surtos_view(
            surtos_from_id=surtos_from_id,
            color=0x8338ec,
            title='Lista de surtos',
            description='Ordenada do mais recente ao mais antigo.')
    await context.channel.send(embed=view.starting_page, view=view)


async def stats(id: int, channel: discord.TextChannel, surtos: dict, last_surtos: dict) -> None:
    if not surtos[id]:
        raise BotError('A lista de surtos está vazia.')
    amount = len(surtos[id])
    date, reason = last_surtos[id]
    ultimo_surto_datetime = datetime.datetime.strptime(date, '%d/%m/%Y, %H:%M:%S')
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


async def remove(bot: commands.Bot, context: commands.Context, surtos: dict):
    id = context.guild.id
    surtos_from_id: list = surtos[id].copy()
    surtos_from_id.sort(reverse=True)
    view = utils.surtos_view(
            surtos_from_id=surtos_from_id,
            color=0xfb5607,
            title='Remover surto',
            description='Digite o número correspondente ao surto a ser removido.')
    await context.channel.send(embed=view.starting_page, view=view)
    msg = await bot.wait_for('message')
    print(msg.content, surtos_from_id[int(msg.content) - 1]) # Now it's just verification, removal from the list and saving.


# Embed color palette:
#   yellow: ffbe0b, orange: fb5607, pink: ff006e, purple: 8338ec, blue: 3a86ff