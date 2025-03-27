import discord
from decouple import config
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=config("COMMAND_PREFIX"), intents=intents)


@bot.event
async def on_ready():
    print(f"Logged on as, {bot.user}")

async def load_cogs():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(config("DISCORD_TOKEN"))

asyncio.run(main())