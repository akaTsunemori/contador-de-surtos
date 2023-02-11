import discord
import json
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv, makedirs
from os.path import exists


if not exists('./database/'):
    makedirs('./database/')


# Client setup
intents =  discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='&', intents=intents)
client.remove_command('help')


# surtos[id] = [(data, surto), ...]: list
surtos = dict()


def bot_setup() -> None:
    for guild in client.guilds:
        id = guild.id
        try:
            surtos_db = open(f'./database/{id}.json', 'r')
            surtos[id] = json.load(surtos_db)
            surtos_db.close()
        except FileNotFoundError:
            # Initialize "create database" event
            pass


@client.event
async def on_ready() -> None:
    bot_setup()
    print('Contador de surtos está pronto!')


load_dotenv('./token.env')
client.run(getenv('TOKEN'))
