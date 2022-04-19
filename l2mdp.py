import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
from dotenv import load_dotenv

import os
load_dotenv(dotenv_path="config")

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.command()
async def Bonjour(ctx):
    await ctx.send("Bonjour !")

@bot.command()
async def l2mdp(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        await ctx.send("Coucou c'est moi !")
        vc.play(discord.FFmpegPCMAudio(executable='ffmpeg', source='Z:\Musiques\Les2minutesdupeupleTrack001.mp3'))

    else:
        await ctx.send("Connectez vous a un channel vocal en premier.")

bot.run(os.getenv("TOKEN"))