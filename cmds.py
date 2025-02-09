import discord
from discord.ext import commands
from monitoring import add_monitor, show_monitor, delete_monitor
from bypass import bypass_link
from shorturl import shorten_url
from genbasic import send_gen_panel
from genbooster import send_gen_booster  # Import fungsi dari genbooster.py

ROLE_ID = 1334790082208596010  # Only Admin

def has_permission(ctx):
    return any(role.id == ROLE_ID for role in ctx.author.roles)

def setup(bot):
    @bot.command()
    async def AddMonitor(ctx, words: str, channel1: discord.TextChannel, channeledit: discord.TextChannel, monitor_name: str):
        if not has_permission(ctx):
            await ctx.send("🚫 **Only Admins can use this command!**")
            return
        await add_monitor(ctx, words, channel1, channeledit, monitor_name)

    @bot.command()
    async def ShowMonitor(ctx):
        if not has_permission(ctx):
            await ctx.send("🚫 **Only Admins can use this command!**")
            return
        await show_monitor(ctx)

    @bot.command()
    async def DelMonitor(ctx, monitor_name: str):
        if not has_permission(ctx):
            await ctx.send("🚫 **Only Admins can use this command!**")
            return
        await delete_monitor(ctx, monitor_name)

    @bot.command()
    async def bypass(ctx, link: str):
        await bypass_link(ctx, link)

    @bot.command()
    async def shorturl(ctx, url: str):
        await shorten_url(ctx, url)

    @bot.command()
    async def genpanelbasic(ctx):
        if not has_permission(ctx):
            await ctx.send("🚫 **Only Admins can use this command!**")
            return
        await send_gen_panel(ctx)

    @bot.command()
    async def genpanelbooster(ctx):
        if not has_permission(ctx):
            await ctx.send("🚫 **Only Admins can use this command!**")
            return
        await send_gen_booster(ctx)  # Panggil fungsi dari genbooster.py

    @bot.command()
    async def cmds(ctx):
        embed = discord.Embed(title="📜 Bot Commands", color=0x3498db)
        embed.add_field(name=".AddMonitor {channel1} {channeledit} {monitor_name}", value="Only Admin! Start monitoring messages in a channel.", inline=False)
        embed.add_field(name=".ShowMonitor", value="Only Admin! Show all active monitors.", inline=False)
        embed.add_field(name=".DelMonitor {monitor_name}", value="Only Admin! Delete a monitor.", inline=False)
        embed.add_field(name=".bypass {link}", value="For Everyone! Bypass a link.", inline=False)
        embed.add_field(name=".shorturl {url}", value="For Everyone! Shortening long url.", inline=False)
        embed.add_field(name=".genpanelbasic", value="Only Admin! Open the basic account generator panel.", inline=False)
        embed.add_field(name=".genpanelbooster", value="Only Admin! Open the booster account generator panel.", inline=False)

        await ctx.send(embed=embed)