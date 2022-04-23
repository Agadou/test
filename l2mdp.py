import discord
import random
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
        nbAleatoire = random.randint(1,5)
        chemin = 'Z:\Musiques\Les2minutesdupeuple Track 00' + str(nbAleatoire) + '.mp3'
        await ctx.send('**Now playing:** {}'.format(chemin))
        vc.play(discord.FFmpegPCMAudio(executable='ffmpeg', source=chemin))
        vc.is_playing()
    else:
        await ctx.send("Connectez vous a un channel vocal en premier.")

@bot.command()
async def pause(ctx):
    voice_client = ctx.author.voice.channel
    if ctx.voice_client.is_playing():
        await ctx.voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
@bot.command()
async def quit(ctx):
    await ctx.voice_client.disconnect()

@bot.command()
async def join(ctx):
    await ctx.author.voice.channel.connect()

@bot.command()
async def logout(ctx):
    await bot.close()

bot.run(os.getenv("TOKEN"))