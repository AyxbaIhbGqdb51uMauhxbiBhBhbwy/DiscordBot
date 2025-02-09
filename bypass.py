import discord
import aiohttp
import datetime

async def bypass_link(ctx, link):
    msg = await ctx.send("Bypassing....")

    api_url = f"https://slr.kys.gay/api/v3/premium/bypass?url={link}&apikey=SLR-35B7E17481BBC37842D10D05D2360FD064201D855D4DEF280DC703FFF1018540016365B54FC96B132D17D8C71EC266F9936745168A70976A091FC7037B22E8B4-jova3435"

    async with aiohttp.ClientSession() as session:
        async with session.get(api_url) as response:
            if response.status == 200:
                data = await response.json()
                bypass_result = data.get("result", "No result found")
                bypass_time = data.get("time", "Unknown")
                status = data.get("status", "Unknown")

                embed = discord.Embed(
                    title="<a:Verify_cyan:1335249212601794652> Bypass Successful!",
                    description="Here is your bypassed link:",
                    color=0x2ecc71,
                    timestamp=datetime.datetime.utcnow()
                )
                embed.add_field(name="<:King_Pepe:1335222278962548776> Bypassed Link", value=f"```{bypass_result}```\n{result}", inline=False)
                embed.add_field(name="<a:clock:1337728212502974496> Process Time", value=f"```{time}```", inline=True)
                embed.add_field(name="<a:spinning_skull:1337730274959691787> Status", value=f"```{status}```", inline=True)
                embed.set_footer(text="Bypass Service - Made by CodeE4X")

                await msg.edit(content="", embed=embed)
            
            else:
                embed = discord.Embed(
                    title="<a:Verify_Red:1335223527011520593> Bypass Failed!",
                    description="The API is offline or unresponsive.",
                    color=0xe74c3c,
                    timestamp=datetime.datetime.utcnow()
                )
                embed.set_footer(text="Bypass Service - Please try again later.")

                await msg.edit(content="", embed=embed)