import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
# Префікс
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def Hello(ctx):
    await ctx.cend("Hello World!")

bot.run('TOKEN')