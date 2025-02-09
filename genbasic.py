import discord
import aiohttp
from discord.ui import View, Button

API_KEY = "nsnseuhusdjcneusbbeuuisefb-OWNERONLY"

class GenBasicView(View):
    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.ctx = ctx

    async def disable_buttons(self):
        for item in self.children:
            item.disabled = True
        await self.message.edit(view=self)
        
    @discord.ui.button(label="Roblox", style=discord.ButtonStyle.primary, emoji="🎮")
    async def roblox_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("🔄 Generating... Please wait 15s", ephemeral=True)
        await self.generate_account(interaction, "Roblox")

    @discord.ui.button(label="Steam", style=discord.ButtonStyle.primary, emoji="🎮")
    async def steam_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("🔄 Generating... Please wait 15s", ephemeral=True)
        await self.generate_account(interaction, "Steam")

    @discord.ui.button(label="Crunchyroll", style=discord.ButtonStyle.primary, emoji="📺")
    async def crunchyroll_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_message("🔄 Generating... Please wait 15s", ephemeral=True)
        await self.generate_account(interaction, "Crunchyroll")

    async def generate_account(self, interaction, service):
        await self.disable_buttons()
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://generator-acc.vercel.app/api/{service}?apikey={API_KEY}") as response:
                if response.status == 200:
                    data = await response.json()
                    embed = discord.Embed(title="🎉 Thank you for using Our Gen", color=0x181818)
                    embed.add_field(name="👤 Username:", value=f"```{data['username']}```", inline=False)
                    embed.add_field(name="🔑 Password:", value=f"```{data['password']}```", inline=False)
                    embed.add_field(name="🛠 Service:", value=f"**{data['Service']}**", inline=False)
                    embed.set_footer(text="Made By CodeE4X | Star X Hub")
                    embed.set_thumbnail(url=interaction.user.avatar.url)
                    embed.set_image(url="https://cdn.discordapp.com/attachments/1250837600705450035/1252915992523178127/standard_3.gif")
                    await interaction.user.send(embed=embed)
                    await interaction.followup.send("✅ Check your DM to claim your account!", ephemeral=True)
                else:
                    await interaction.response.send_message("❌ Failed to generate an account. Please try again later.", ephemeral=True)

async def send_gen_panel(ctx):
    embed = discord.Embed(title="✨ Star X Gen Service", description="Select one service by pressing a button.\n\nBoost our Server to get More Service!", color=0x3498db)
    view = GenBasicView(ctx)
    view.message = await ctx.send(embed=embed, view=view)