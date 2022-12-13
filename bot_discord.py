import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('')
client = discord.Client("OTc1OTk4MzMyNjkyNDY3NzUy.GgQywW.7NMVcvMWzCj63gGDaWlMQ0G-fLX6tG_hJspMAE")

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
    
client.run(TOKEN)