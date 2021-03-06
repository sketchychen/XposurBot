from datetime import datetime

@bot.event
async def on_command_error(context, error):
    print('on_command_error fired')
    if isinstance(error, commands.errors.CheckFailure):
        # example decorator that may trigger this exception: @commands.has_role('admin')
        await context.send('You do not have the correct role for this command.')
    else:
        with open('err.log', 'a+') as file:
            file.write(
                f'[{datetime.now()}] Unhandled exception:\n'
                f'{context.__dict__}\n'
                f'{error}\n'
            )