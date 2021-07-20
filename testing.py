import json
import discord 
from discord.ext import commands
import requests

client = discord.Client()
client = commands.Bot(command_prefix="!")

keywords = ["ywl gay"]

@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for i in range(10):
                    await message.channel.send("No Fuck u")

client.run('ODUxNzY2MDk5NDQ2OTg4ODEx.YL9C_w.GKmNqVSZjDMOjSlVljLqSGd0RFc')