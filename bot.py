import discord
from discord.ext import commands, tasks
import cmds

TOKEN = "MTMzNzIwNzM1ODYwMTgyMjM4MA.Go-Obp.BcZxekN9hdPEG0wVqxMsbjeCjSimy9Z1_dwh14"
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")
    update_status.start()

@tasks.loop(seconds=10)
async def update_status():
    guilds = bot.guilds
    members = sum(guild.member_count for guild in guilds)
    statuses = [
        f" {members} User!",
        f" {len(guilds)} Server!",
        " .cmds Command!",
        " https://discord.gg/juRYbcKdYW"
    ]
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=statuses[update_status.current_loop % len(statuses)]))

cmds.setup(bot)
bot.run(TOKEN)