# Work with Python 3.6
import os
import discord
import asyncio
from models import Skill
from helpers import boot_database
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN", "")

client = discord.Client()


def clean_content(content, string):
    return content[len(string) :].strip()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith("!skill "):
        boot_database()
        skill_name = clean_content(message.content, "!skill")
        skill_search = Skill.where("string", "like", "%{}%".format(skill_name))
        count = skill_search.count()
        if count == 0:
            await message.channel.send(
                'Couldn\'t find any skills similar to "{}".'.format(skill_name)
            )
        elif count == 1:
            skill = skill_search.first()
            await message.channel.send("", embed=skill.generateEmbed())
        else:
            skill = skill_search.first()
            await message.channel.send("", embed=skill.generateEmbed())


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


client.run(TOKEN)
