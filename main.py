import discord
import json
from discord.ext import commands, tasks
from dotenv import load_dotenv
from os import getenv, makedirs
from os.path import exists


import src.commands as cmd
import src.utils as utils
import src.tasks
from src.bot_error import BotError


if not exists('./database/'):
    makedirs('./database/')


# bot setup
intents =  discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
bot.remove_command('help')


surtos = dict()                 # surtos[id] = [(data, surto), ...]: list
last_surtos = dict()            # last_surtos[id] = (data, surto)


async def bot_setup() -> None:
    for guild in bot.guilds:
        id = guild.id
        if not (exists(f'./database/{id}.json') and exists(f'./database/{id}_last.json')):
            surtos[id] = list()
            last_surtos[id] = list()
            utils.save(id, surtos, last_surtos)
        surtos_db = open(f'./database/{id}.json', 'r')
        last_surto_db = open(f'./database/{id}_last.json', 'r')
        surtos[id] = json.load(surtos_db)
        last_surtos[id] = json.load(last_surto_db)
        surtos_db.close()
        last_surto_db.close()
        channel_check = [i for i in guild.text_channels if i.name == 'contador-de-surtos']
        if not channel_check:
            await guild.create_text_channel('contador-de-surtos')
        role_check = [i for i in guild.roles if i.name == 'Gerente de Surtos']
        if not role_check:
            await guild.create_role(name='Gerente de Surtos')


# Bot tasks
@tasks.loop(hours=1)
async def background_task() -> None:
    try:
        await src.tasks.daily_stats(bot, surtos, last_surtos)
    except BotError:
        return


# Bot events
@bot.event
async def on_ready() -> None:
    await bot_setup()
    background_task.start()
    print('Contador de surtos está pronto!')


@bot.event
async def on_guild_join(guild: discord.Guild) -> None:
    id = guild.id
    if not (exists(f'./database/{id}.json') and exists(f'./database/{id}_last.json')):
        surtos[id] = list()
        last_surtos[id] = list()
        utils.save(id, surtos, last_surtos)
    await guild.create_text_channel('contador-de-surtos')
    await guild.create_role(name='Gerente de Surtos')


# Bot commands
@bot.command(name='surto')
async def _surto(context: commands.Context, *args) -> None:
    try:
        await cmd.surto(context, surtos, last_surtos, args)
    except BotError as e:
        await context.channel.send(str(e))


@bot.command(name='surtos')
async def _surtos(context: commands.Context, *args) -> None:
    try:
        await cmd.surtos(context, surtos)
    except BotError as e:
        await context.channel.send(str(e))


@bot.command(name='stats')
async def _stats(context: commands.Context, *args) -> None:
    try:
        await cmd.stats(context.guild.id, context.channel, surtos, last_surtos)
    except BotError as e:
        await context.channel.send(str(e))


@bot.command(name='reset')
async def _reset(context: commands.Context, *args) -> None:
    try:
        await cmd.reset(context, args, surtos, last_surtos)
    except BotError as e:
        await context.channel.send(str(e))


@bot.command(name='remove')
async def _remove(context: commands.Context, *args) -> None:
    try:
        await cmd.remove(bot, context, surtos, last_surtos)
    except BotError as e:
        await context.channel.send(str(e))


@bot.command(name='help')
async def _help(context: commands.Context, *args) -> None:
    try:
        await cmd.help(context)
    except BotError as e:
        await context.channel.send(str(e))


# Load token and run bot
load_dotenv('./token.env')
bot.run(getenv('TOKEN'))
