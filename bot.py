import discord
from discord.ext import commands, tasks
from decouple import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config("COMMAND_PREFIX"), intents=intents)

@bot.event
async def on_ready():
    print('Logged on as', bot.user)

@bot.command()
async def test(ctx, arg):
    print(ctx)
    await ctx.send(arg)
    


bot.run(config("DISCORD_TOKEN"))