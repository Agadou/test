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

@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.author.voice.channel
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

bot.run(os.getenv("TOKEN"))