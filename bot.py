import discord
import modelpy as mp
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./uploads/{attachment.filename}")
            await ctx.send(f"Hehmm... Kelihatanya seru. Aku taro di uploads/ he hihihi!")
    else:
        await ctx.send("Ngga ada gambar=ngga ada seru phhhhh....")

@bot.command()
async def dos(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url

            await attachment.save(f"./uploads/{attachment.filename}")
            classs=mp.guess(f"./uploads/{attachment.filename}")
            await ctx.send(f"Hmm... Aku rasa ini adalah: {classs} ")

    else:
        await ctx.send("NGGA ADA GAMBAR MASA MAU KLASIFIKASI SIHHH????")

bot.run("HERE GOES YOUR TOKEN")
