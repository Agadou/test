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
    if ctx.author.voice: #Si l'auteur du message est dans un channel vocal
        channel = ctx.author.voice.channel
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice is None or not voice.is_connected():
            vc = await channel.connect()
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        nbAleatoire = random.randint(1,5)
        chemin = 'Z:\Musiques\Les2minutesdupeuple Track 00' + str(nbAleatoire) + '.mp3'
        await ctx.send('**Now playing:** {}'.format(chemin))
        voice.play(discord.FFmpegPCMAudio(executable='ffmpeg', source=chemin))
        voice.is_playing()
    else: #Si l'auteur du message n'est pas dans un channel vocal, on indique un message
        await ctx.send("Connectez vous a un channel vocal en premier.")

@bot.command()
async def pause(ctx):
    voice_client = ctx.author.voice.channel
    if ctx.voice_client.is_playing():
        ctx.voice_client.pause()
    else:
        await ctx.send("Le bot ne joue rien en ce moment.")

@bot.command()
async def resume(ctx):
    voice_client = ctx.author.voice.channel
    if ctx.voice_client.is_paused():
        ctx.voice_client.resume()
    else:
        await ctx.send("Le bot n'est pas en pause.")


@bot.command()
async def quit(ctx):
    if ctx.author.voice:
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("Connectez vous a un channel vocal en premier.")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
    else:
        await ctx.send("Connectez vous a un channel vocal en premier.")

@bot.command()
async def logout(ctx):
    await bot.change_presence(status=discord.Status.offline)
    await ctx.voice_client.disconnect()
    await bot.close()

bot.run(os.getenv("TOKEN"))