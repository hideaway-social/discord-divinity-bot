# Work with Python 3.6
import os
import discord
import asyncio
from models import Skill, Search, Build, School
from helpers import boot_database
from dotenv import load_dotenv
import hunspell

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
    hobj = hunspell.HunSpell('dictionaries/en_US.dic', 'dictionaries/en_US.aff')
    if message.content.startswith("!suggest "):
        string = clean_content(message.content, "!suggest")
        if(not hobj.spell(string)):
            await message.channel.send("Did you maybe mean \"" + hobj.suggest(string)[0] + "\"?")
        else:
            await message.channel.send("Seems fine to me.")

    if message.content.startswith("!search "):
        string = clean_content(message.content, "!search")
        data = Search(string)
        await message.channel.send("", embed=data.performSearch())

    if message.content.startswith("!build "):
        boot_database()
        build_name = clean_content(message.content, "!build")
        if(not hobj.spell(build_name)):
            builds_collection = Build.where("string", "like", "%{}%".format(build_name)).get()
            for suggestion in hobj.suggest(build_name)[:2]:
                builds_collection.merge(Build.where("string", "like", "%{}%".format(suggestion)).get())
            builds_collection.unique()
        else:
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
        if(not hobj.spell(skill_name)):
            skills_collection = Skill.where("string", "like", "%{}%".format(skill_name)).get()
            for suggestion in hobj.suggest(skill_name)[:2]:
                skills_collection.merge(Skill.where("string", "like", "%{}%".format(suggestion)).get())
            skills_collection.unique()
        else:
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
