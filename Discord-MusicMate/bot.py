import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

music_queue = []

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}
FFMPEG_OPTIONS = {'options': '-vn'}

@bot.event
async def on_ready():
    print(f'✅ Logged in as {bot.user}')

async def play_next(ctx):
    if len(music_queue) > 0:
        url = music_queue.pop(0)
        with yt_dlp.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['url']
            title = info.get('title', 'Unknown')
            voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
            voice.play(discord.FFmpegPCMAudio(url2, **FFMPEG_OPTIONS),
                       after=lambda e: asyncio.run_coroutine_threadsafe(play_next(ctx), bot.loop))
        await ctx.send(f"🎶 Now playing: **{title}**")
    else:
        voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice and voice.is_connected():
            await voice.disconnect()

@bot.command(name='play')
async def play(ctx, *, search: str):
    voice_channel = ctx.author.voice.channel if ctx.author.voice else None
    if not voice_channel:
        await ctx.send("❌ You need to join a voice channel first.")
        return

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice:
        await voice_channel.connect()

    if "youtube.com" in search or "youtu.be" in search:
        url = search
    else:
        with yt_dlp.YoutubeDL({'quiet': True, 'format': 'bestaudio', 'default_search': 'ytsearch'}) as ydl:
            info = ydl.extract_info(search, download=False)
            url = info['entries'][0]['webpage_url']
    music_queue.append(url)
    await ctx.send(f"✅ Added to queue: {search}")

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if not voice.is_playing():
        await play_next(ctx)

@bot.command()
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.pause()
        await ctx.send("⏸️ Paused.")

@bot.command()
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_paused():
        voice.resume()
        await ctx.send("▶️ Resumed.")

@bot.command()
async def skip(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.stop()
        await ctx.send("⏭️ Skipped.")

@bot.command()
async def queue(ctx):
    if len(music_queue) == 0:
        await ctx.send("🎶 Queue is empty.")
    else:
        queue_list = "\n".join([f"{i+1}. {url}" for i, url in enumerate(music_queue)])
        await ctx.send(f"📜 **Queue:**\n{queue_list}")

@bot.command()
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice:
        music_queue.clear()
        await voice.disconnect()
        await ctx.send("🛑 Stopped and disconnected.")

TOKEN = os.getenv("DISCORD_TOKEN") or "YOUR_BOT_TOKEN_HERE"
bot.run(TOKEN)
