import discord
import aiohttp
import datetime

async def shorten_url(ctx, url):
    msg = await ctx.send("🔗 Shortening URL...")

    api_url = f"http://tinyurl.com/api-create.php?url={url}"

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                short_url = await response.text()

                embed = discord.Embed(
                    title="🔗 URL Shortened Successfully!",
                    description="Here is your shortened URL:",
                    color=0x3498db,
                    timestamp=datetime.datetime.utcnow()
                )
                embed.add_field(name="🔗 Original URL", value=f"```{url}```", inline=False)
                embed.add_field(name="🌐 Shortened URL", value=f"[{short_url}]({short_url})", inline=False)
                embed.set_footer(text="URL Shortener - Powered by TinyURL Api")

                await msg.edit(content="", embed=embed)

            else:
                embed = discord.Embed(
                    title="❌ URL Shortening Failed!",
                    description="The API is offline or unresponsive.",
                    color=0xe74c3c,
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="URL Shortener - Please try again later.")

                await msg.edit(content="", embed=embed)