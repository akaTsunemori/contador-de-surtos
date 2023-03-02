import discord
import json
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv, makedirs
from os.path import exists


import src.commands as commands
import src.events as events
import src.utils as utils
from src.bot_error import BotError


if not exists('./database/'):
    makedirs('./database/')


# bot setup
intents =  discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='&', intents=intents)
bot.remove_command('help')


# surtos[id] = [(data, surto), ...]: list
surtos = dict()
last_surtos = dict()


def bot_setup() -> None:
    for guild in bot.guilds:
        id = guild.id
        try:
            surtos_db = open(f'./database/{id}.json', 'r')
            last_surto_db = open(f'./database/{id}_last.json', 'r')
            surtos[id] = json.load(surtos_db)
            last_surtos[id] = json.load(last_surto_db)
            surtos_db.close()
            last_surto_db.close()
        except FileNotFoundError:
            # Create DB
            pass


# Bot events
@bot.event
async def on_ready() -> None:
    bot_setup()
    print('Contador de surtos está pronto!')


@bot.event
async def on_guild_join(guild: discord.Guild) -> None:
    pass
    # await events.on_guild_join()


# Bot commands
@bot.command(name='surto')
@commands.has_permissions(administrator=True) # These perms should be modified
async def _surto(context: commands.Context, *args) -> None:
    try:
        await commands.surto(context, args,)
    except BotError as e:
        await context.channel.send(str(e))


load_dotenv('./token.env')
bot.run(getenv('TOKEN'))
