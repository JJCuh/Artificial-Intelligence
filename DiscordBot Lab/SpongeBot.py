# SpongeBot.py
# By: Justin Li

import os
import discord
import env
import markovify

from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=env.guild)

    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

    print(
        'Hey there! My name is Spongebot Squarepants.\n'
        'To make me to say something, type \"!talk\"\n'
        'Hope you have fun, cuz I\'m ready!'
    )


@bot.command(name = 'talk', help = 'SpongeBot will say a line')
async def talk(ctx):

    # Get raw text as string.
    with open("./SpongeBot.txt") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.Text(text)
    
    # Creates a randomly-generated line of no more than 100 characters
    line = text_model.make_short_sentence(100)
    await ctx.send(line)

bot.run(env.token)