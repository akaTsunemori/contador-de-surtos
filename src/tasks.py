from datetime import datetime
from discord.ext import commands


import src.commands as cmd


async def daily_stats(bot: commands.Bot, surtos: dict, last_surtos: dict) -> None:
    dt = datetime.now()
    if dt.hour != 12:
        return
    for guild in bot.guilds:
        channel_id = [i.id for i in guild.text_channels if i.name == 'contador-de-surtos'][0]
        channel = bot.get_channel(channel_id)
        await cmd.stats(guild.id, channel, surtos, last_surtos)