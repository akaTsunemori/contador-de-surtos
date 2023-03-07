import discord
import json
from discord.ext import commands, tasks
from dotenv import load_dotenv
from os import getenv, makedirs
from os.path import exists


import src.commands as cmd
import src.events as events
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
            last_surtos[id] = tuple()
            utils.save(id, surtos, last_surtos)
        surtos_db = open(f'./database/{id}.json', 'r')
        last_surto_db = open(f'./database/{id}_last.json', 'r')
        surtos[id] = json.load(surtos_db)
        last_surtos[id] = json.load(last_surto_db)
        surtos_db.close()
        last_surto_db.close()
        channel_id = [i.id for i in guild.text_channels if i.name == 'contador-de-surtos']
        if not channel_id:
            await guild.create_text_channel('contador-de-surtos')


# Bot tasks
@tasks.loop(hours=1)
async def background_task() -> None:
    try:
        await src.tasks.daily_stats(bot, surtos, last_surtos)
    except BotError as e:
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
        last_surtos[id] = tuple()
        utils.save(id, surtos, last_surtos)
    await guild.create_text_channel('contador-de-surtos')


# Bot commands
@bot.command(name='surto')
@commands.has_permissions(administrator=True) # These perms should be modified for every cmd
async def _surto(context: commands.Context, *args) -> None:
    try:
        await cmd.surto(context, surtos, last_surtos, args)
    except BotError as e:
        await context.channel.send(str(e))


@bot.command(name='surtos')
@commands.has_permissions(administrator=True)
async def _surtos(context: commands.Context, *args) -> None:
    try:
        await cmd.surtos(context, surtos)
    except BotError as e:
        await context.channel.send(str(e))


@bot.command(name='stats')
@commands.has_permissions(administrator=True)
async def _stats(context: commands.Context, *args) -> None:
    try:
        await cmd.stats(context.guild.id, context.channel, surtos, last_surtos)
    except BotError as e:
        await context.channel.send(str(e))


# Load token and run bot
load_dotenv('./token.env')
bot.run(getenv('TOKEN'))
