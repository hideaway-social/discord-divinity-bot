# Work with Python 3.6
import os
import discord
import asyncio
from models import Search
from orator import Collection
from helpers import boot_database, clean_content
from dotenv import load_dotenv
import hunspell
from responders import SkillResponder, BuildResponder

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN", "")

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith("!suggest "):
        string = clean_content(message.content, "!suggest")
        hobj = hunspell.HunSpell('dictionaries/en_US.dic', 'dictionaries/en_US.aff')
        if(not hobj.spell(string)):
            await message.channel.send("Did you maybe mean \"" + hobj.suggest(string)[0] + "\"?")
        else:
            await message.channel.send("Seems fine to me.")

    if message.content.startswith("!search "):
        string = clean_content(message.content, "!search")
        data = Search(string)
        await message.channel.send("", embed=data.performSearch())

    if message.content.startswith("!build "):
        await message.channel.send(**BuildResponder(message).getReply())

    if message.content.startswith("!skill "):
        await message.channel.send(**SkillResponder(message).getReply())

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


client.run(TOKEN)
