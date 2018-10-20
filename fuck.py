import time

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="fuck you")

@bot.event
async def on_ready():
	print("We're ready")
	time.sleep(99999999999999)
	
bot.run("fuck you")