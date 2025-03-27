import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("General")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("🏓 Pong!")

    @commands.command()
    async def say(self, ctx):
        await ctx.send("pong")

async def setup(bot):
    await bot.add_cog(General(bot))