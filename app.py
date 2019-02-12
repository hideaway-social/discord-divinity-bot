# Work with Python 3.6
import os
import discord
import asyncio
from models import Skill, Search, Build, School
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

    if message.content.startswith("!search "):
        string = clean_content(message.content, "!search")
        data = Search(string)
        await message.channel.send("", embed=data.performSearch())

    if message.content.startswith("!build "):
        boot_database()
        build_name = clean_content(message.content, "!build")
        builds_collection = Build.where("string", "like", "%{}%".format(build_name)).get()
        count = builds_collection.count()
        if count == 0:
            await message.channel.send(
                'Couldn\'t find any builds similar to "{}".'.format(build_name)
            )
        elif count == 1:
            build = builds_collection.first()
            await message.channel.send("", embed=build.generateSingleEmbed())
        else:
            await message.channel.send("", embed=Build.generateMultiEmbed(builds_collection))

    if message.content.startswith("!skill "):
        boot_database()
        skill_name = clean_content(message.content, "!skill")
        skills_collection = Skill.where("string", "like", "%{}%".format(skill_name)).get()
        count = skills_collection.count()
        if count == 0:
            await message.channel.send(
                'Couldn\'t find any skills similar to "{}".'.format(skill_name)
            )
        elif count == 1:
            skill = skills_collection.first()
            await message.channel.send("", embed=skill.generateSingleEmbed())
        else:
            await message.channel.send("", embed=Skill.generateMultiEmbed(skills_collection))


@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")


client.run(TOKEN)
