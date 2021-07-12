import discord
import os
import datetime
from dotenv import load_dotenv
from discord.ext import commands

# local imports
import logger

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = commands.Bot(command_prefix='&')

@bot.event
async def on_ready():
    # discord.utils.get returns first element in iterable
    guild = discord.utils.get(bot.guilds)
    message = (
        f'{bot.user} connected to the following guild:\n'
        f'{guild.name} (id: {guild.id})'
    )

    logger.audit(message)

    print(message)


@bot.command(
    name='hello',
    help='test command'
)
async def hello_world(context: commands.Context):
    print('hello_world', context)
    await context.send('okay weirdo')


@bot.event
async def on_command_error(context, error):
    print('on_command_error fired')
    if isinstance(error, commands.errors.CheckFailure):
        # example decorator that may trigger this exception: @commands.has_role('admin')
        await context.send('You do not have the correct role for this command.')
    else:
        with open('err.log', 'a+') as file:
            file.write(
                f'[{datetime.datetime.now()}] Unhandled exception:\n'
                f'{context.__dict__}\n'
                f'{error}\n'
            )


bot.run(TOKEN)
