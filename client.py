# client.py
import os
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

# https://i.stack.imgur.com/ICWVL.gif
client = discord.Client()


## RESPONDING TO SELF CONNECTION/GOING ONLINE ##
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds)

    print(
        f'{client.user} is connected to the following guild(s):\n'
        f'{guild.name} (id: {guild.id})'
    )


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
