print('starting')
import guilded
from guilded.ext import commands
import os
from replit_keep_alive import WaitressStart
WaitressStart()


botprefix = '-' # <-- The prefix you want here

bot = commands.Bot(command_prefix=botprefix) #define bot and setup a prefix

# notifies when the bot is ready
@bot.event
async def on_ready():
  print("Bot is up and ready!")

@bot.command()
async def ping(ctx):
  """Pong"""
  await ctx.send(f'Pong! `{round (bot.latency * 1000)}` ms')

@bot.command()
async def say(ctx, *, message="You didn't give a message"):
  """Echo's you"""
  await ctx.delete()
  await ctx.send(message)

bot.run(os.environ['TOKEN']) #runs the bot on the token from the secrets
