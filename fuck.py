import time

import requests
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="fuck you")

@bot.event
async def on_ready():
	print("We're ready")
	time.sleep(99999999999999)
	
bot.run(requests.get("https://raw.githubusercontent.com/WorstDiscordBots/fuckyou/master/suckmydick").text) # thistbh
