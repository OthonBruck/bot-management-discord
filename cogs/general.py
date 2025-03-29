import discord
from discord.ext import commands
from database.voice_activity import register_entry, register_exit

class TimeManagement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("TimeManagement")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel == after.channel:
            return
        if before.channel == None or before.afk == True:
            await register_entry(member.id, member.guild.id)
            return

        if after.channel == None or after.afk == True:
            await register_exit(member.id, member.guild.id)
            return

async def setup(bot):
    await bot.add_cog(TimeManagement(bot))