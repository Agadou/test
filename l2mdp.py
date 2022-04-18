import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import json

bot = commands.Bot(command_prefix="!")

bot.run("OTY1NjQ4NDA5OTg4MDQyNzUy.Yl2QKQ.XOVMrTivsAnWqoIRawYDx7C4_8g")

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.event
async def on_message(message):
    if message.content.startswith("!play"):
        source = FFmpegPCMAudio("/var/medias/Musiques/Les2minutesdupeuple Track 001.mp3")