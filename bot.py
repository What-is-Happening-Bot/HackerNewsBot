# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

actions = commands.Bot(command_prefix= '!')

@actions.event
async def on_ready():
    print(f'{actions.user} has connected to Discord!')

for filename in os.listdir('./actions'):
    if filename.endswith('.py') and filename != '__init__.py':
        actions.load_extension(f'actions.{filename[:-3]}')

actions.run(TOKEN)
