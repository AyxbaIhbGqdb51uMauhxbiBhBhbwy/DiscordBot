import discord
from discord.ext import tasks

monitored_channels = {}

async def add_monitor(ctx, words, channel1, channeledit, monitor_name):
    words = None if words.lower() == "none" else words
    embed = discord.Embed(title=f"📊 Stats For `{monitor_name}`", color=0x3498db)
    embed.add_field(name="🎯 Execute Count", value="Execute: `0`", inline=False)
    msg = await channeledit.send(embed=embed)
    
    monitored_channels[monitor_name] = {
        "channel": channel1.id,
        "edit_channel": channeledit.id,
        "count": 0,
        "message_id": msg.id,
        "words": words
    }
    
    await ctx.send(f"✅ Monitoring `{monitor_name}` has been set for {channel1.mention}!")

async def show_monitor(ctx):
    if not monitored_channels:
        await ctx.send("🚫 No active monitors found!")
        return
    
    embed = discord.Embed(title="📊 Active Monitors", color=0x3498db)
    for name, data in monitored_channels.items():
        channel = ctx.bot.get_channel(data["channel"])
        embed.add_field(name=f"🟢 {name}", value=f"**Channel:** {channel.mention}\n**Message Count:** `{data['count']}`", inline=False)
    
    await ctx.send(embed=embed)

async def delete_monitor(ctx, monitor_name):
    if monitor_name in monitored_channels:
        del monitored_channels[monitor_name]
        await ctx.send(f"✅ Monitor `{monitor_name}` has been deleted!")
    else:
        await ctx.send(f"🚫 Monitor `{monitor_name}` not found!")

@tasks.loop(minutes=1)
async def monitoring_task():
    for name, data in monitored_channels.items():
        edit_channel = discord.utils.get(bot.get_all_channels(), id=data["edit_channel"])
        if edit_channel:
            try:
                msg = await edit_channel.fetch_message(data["message_id"])
                embed = discord.Embed(title=f"📊 Stats For `{name}`", color=0x3498db)
                embed.add_field(name="📊 Message Count", value=f"Execute: `{data['count']}`", inline=False)
                await msg.edit(embed=embed)
            except discord.NotFound:
                pass