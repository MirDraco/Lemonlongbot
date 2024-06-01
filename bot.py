import discord
from discord.ext import commands

bot = commands.Bot(intents=discord.Intents.all(), command_prefix="!")
@bot.event
async def on_ready():
    print(f"{bot.user} 이(가) 눈을떴다")


@bot.event
async def on_message(message):
    if message.content == "안녕":
        await message.channel.send("안녕!")

bot.run("")
