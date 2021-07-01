# client.py
import os
import discord
import datetime
from dotenv import load_dotenv

# local imports
import logger
from bot import bot


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# https://i.stack.imgur.com/ICWVL.gif
client = discord.Client()


## RESPONDING TO SELF CONNECTION/GOING ONLINE ##
@client.event
async def on_ready():
    # discord.utils.get returns first element in iterable
    guild = discord.utils.get(client.guilds)

    message = (
        f'{client.user} connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

    logger.audit(message)

    print(message)


## RESPONDING TO EXCEPTIONS ##
@client.event
async def on_error(event, *args, **kwargs):
    print(args)
    print(kwargs)
    with open('err.log', 'a+') as f:
        if event == 'on_message':
            f.write(
                f'[{datetime.datetime.now()}] Unhandled message:\n'
                f'{args[0]}\n'
            )
        else:
            raise


client.run(TOKEN)
bot.run(TOKEN)
