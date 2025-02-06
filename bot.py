import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Aku Online"))
    print(f"Bot {bot.user} telah online!")

@bot.command()
async def test(ctx):
    await ctx.send("hi bro")

bot.run("MTMzNzIwNzM1ODYwMTgyMjM4MA.Gds7Zk.N7-i0GGnZ85n2Ce8A0jnLwF-uSOTxQSYcQMflw")
