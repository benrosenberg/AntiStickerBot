# -*- coding: utf-8 -*-
import discord, asyncio, logging, dotenv, os
from discord.ext import commands
from discord.ext.commands import Bot

dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")

description = 'Simple bot that deletes stickers.'

bot = discord.Client()

@bot.event
async def on_ready():
        print('Logged in as: ')
        print(bot.user.name)
        print(bot.user.id)
        print('------------')
        activity = discord.Activity(name = 'for stickers', type = discord.ActivityType.watching)
        await bot.change_presence(activity=activity)

@bot.event
async def on_message(message):
    if message.stickers != []:
        await message.delete()
        await message.channel.send(f"{message.author.mention}, this is a no-sticker server.", delete_after=5)

bot.run(TOKEN)
