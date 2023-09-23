import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот лыотмловатплотавлопитатилдтизоатпиолытваиапралдоип !')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)




bot.run("MTE1MjU3Mzc4OTYyOTA1NTAyNw.GSh9c_.mHpm9n_4rHXCuvZ03XwkuHvG0g1maWMoO5UYd0")