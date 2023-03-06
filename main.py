import discord
import json
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv, makedirs
from os.path import exists


import src.commands as cmd
import src.events as events
import src.utils as utils
from src.bot_error import BotError


if not exists('./database/'):
    makedirs('./database/')


# bot setup
intents =  discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
bot.remove_command('help')


# surtos[id] = [(data, surto), ...]: list
surtos = dict()
# last_surtos[id] = (data, surto)
last_surtos = dict()


def bot_setup() -> None:
    for guild in bot.guilds:
        id = guild.id
        if not (exists(f'./database/{id}.json') and exists(f'./database/{id}_last.json')):
            surtos[id] = list()
            last_surtos[id] = tuple()
            utils.save(id, surtos, last_surtos)
        surtos_db = open(f'./database/{id}.json', 'r')
        last_surto_db = open(f'./database/{id}_last.json', 'r')
        surtos[id] = json.load(surtos_db)
        last_surtos[id] = json.load(last_surto_db)
        surtos_db.close()
        last_surto_db.close()


# Bot events
@bot.event
async def on_ready() -> None:
    bot_setup()
    print('Contador de surtos está pronto!')


@bot.event
async def on_guild_join(guild: discord.Guild) -> None:
    id = guild.id
    if not (exists(f'./database/{id}.json') and exists(f'./database/{id}_last.json')):
        surtos[id] = list()
        last_surtos[id] = tuple()
        utils.save(id, surtos, last_surtos)


# Bot commands
@bot.command(name='surto')
@commands.has_permissions(administrator=True) # These perms should be modified
async def _surto(context: commands.Context, *args) -> None:
    try:
        await cmd.surto(context, surtos, last_surtos, args)
    except BotError as e:
        await context.channel.send(str(e))


@bot.command(name='surtos')
@commands.has_permissions(administrator=True) # These perms should be modified
async def _surtos(context: commands.Context, *args) -> None:
    try:
        await cmd.surtos(context, surtos)
    except BotError as e:
        await context.channel.send(str(e))


load_dotenv('./token.env')
bot.run(getenv('TOKEN'))
