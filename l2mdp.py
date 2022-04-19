import discord
from discord.ext import commands
from discord import FFmpegPCMAudio

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Le bot est prêt.")

@bot.command()
async def Bonjour(ctx):
    await ctx.send("Bonjour !")

@bot.command()
async def l2mdp(ctx):
    # Gets voice channel of message author
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable='ffmpeg', source='Les2minutesdupeupleTrack001.mp3'))

    else:
        await ctx.send("Connectez vous a un channel vocal en premier.")

bot.run("OTY1NjQ4NDA5OTg4MDQyNzUy.Yl2QKQ.XOVMrTivsAnWqoIRawYDx7C4_8g")