import os
import json
import string
import random
import asyncio
import disnake
import traceback
import base64 as b64
from enum import Enum
from disnake.enums import *
from disnake.ext import commands
import extras

def main(token):
    bot = commands.Bot(sync_commands = True)
    bot.change_presence(activity = discord.Game(name = "CKBot"))

    answers = {
        "where": "BruhKoli will be gone for a long time.",
        "bot": "I'm a bot made for Creatorkill because he's cool by bdidk235 mainly for the Generic RPG Game Server.",
        "bot_creation": "I'm made using Python with Disnake, You can also check out the [Source Code](https://github.com/bdidk235/CKBot) for this Bot.",
        "who": "I'm a bot, Made by a person!",
        "bdidk235": "bdidk235 is the developer of CKBot and also develops for the game and other projects.",
        "banana": "In Creatorkill's Basement.",
        "private": "You can use message me and I will still work with the commands.",
        "stealing": "Maybe? Hopefully not!",
        "ron": "Ron.",
        "amogus": "Amogus a.k.a. KonradRon2 is the Owner of Generic RPG Game.",
        "creatorkill": "Creatorkill is a guy who does stuff and my name is based on his username because he's too cool to ignore.",
        "admins": "Admins can do a lot of thing, and moderate the game they have access to admin commands and some other stuff.",
        "bobo": "Bobo :rofl:",
        "suck": "It's not a rickroll, Trust me! <https://www.youtube.com/watch?v=dQw4w9WgXcQ>",
        "suck2": "You suck at using me, You couldn't have scrolled down here!",
        "idiot": "You are probably The REAL Idiot or but maybe I am...",
        "why": "Why not?",
    }

    speach_types = [
        "Yes",
        "No",
        "Maybe",
        "I'm not smart",
        "What you think you are?",
        "I met a person before!",
        "NO, YOU THATS COMPLETELY WRONG!",
        "WHERE IS $username, I CANT FIND THEM!",
        "You are an idiot!",
        "$username PLEASE STOP!",
        "no u",
        "I don't steal, I ask for it!",
        "I'm stupid",
        "THIS IS SO IRONIC",
        "START RUNNING NOW!",
        "Ok.",
        "Cancel it.",
        "You're Cancelled!",
    ]

    jumpscares = [
        "https://tenor.com/view/dog-dog-jumpscare-jumpscare-jumpscare-gif-the-dog-gif-23747153",
        "https://tenor.com/view/sogga-big-floppa-caracal-floppa-big-soggus-gif-23364768",
        "https://tenor.com/view/markiplier-jumpscare-punch-fnaf-gif-23353403",
        "https://tenor.com/view/gaster-wd-gaster-undertale-undertale-gaster-gaster-jumpscare-gif-24147829",
        "https://tenor.com/view/jump-scare-gif-18504612",
        "https://tenor.com/view/the-rock-the-rock-jumpscare-the-rock-sussy-gif-24038148",
        "https://tenor.com/view/omori-omori-sunny-sunny-omori-jumpscare-gif-24352720",
        "https://tenor.com/view/among-us-amogus-jumpscare-jumpscare-gif-among-us-sus-gif-24082720",
    ]

    @bot.slash_command(
        description = "Frequently Asked questions.",
        options = [
            disnake.Option("question", "What is your question?", disnake.OptionType.string, True, choices = [
                disnake.OptionChoice("WHERE IS HE?", "where"),
                disnake.OptionChoice("What are you?", "bot"),
                disnake.OptionChoice("How are you made?", "bot_creation"),
                disnake.OptionChoice("Who is bdidk235?", "bdidk235"),
                disnake.OptionChoice("Where is the Banana?", "banana"),
                disnake.OptionChoice("Are you just an FAQ Bot?", "faq"),
                disnake.OptionChoice("Can I use you privately?", "private"),
                disnake.OptionChoice("Is There a Stealing Problem?", "stealing"),
                disnake.OptionChoice("Who is Ron?", "ron"),
                disnake.OptionChoice("Who is Amogus?", "amogus"),
                disnake.OptionChoice("Who is Creatorkill?", "creatorkill"),
                disnake.OptionChoice("What Admins do?", "admins"),
                disnake.OptionChoice("What does Bobo Mean?", "bobo"),
                disnake.OptionChoice("Do You Suck at everything?", "suck"),
                disnake.OptionChoice("Do You Suck at something?", "suck2"),
                disnake.OptionChoice("Are you an Idiot?", "idiot"),
                disnake.OptionChoice("Who is You?", "who"),
                disnake.OptionChoice("Why?", "why"),
            ])
        ]
    )
    async def faq(inter, question: str):
        if question == "faq":
            await inter.send("I can also randomly rickroll you!")
            try:
                searches = ["rickroll", "rick roll", "never gonna give you up"]
                search = random.choice(searches)
                videos = extras.youtube_search(search, 25)
                await inter.send(random.choice(videos)["link"])
            except Exception:
                await inter.send("A Totally Random Rickroll: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                traceback.print_exc()
            return

        await inter.send(answers[question])

    @bot.slash_command(
        description = "yoy"
    )
    async def yoy(inter):
        await inter.send("yoy <:yoy1:943929050097938453><:yoy2:943929050093748255>")

    @bot.slash_command(
        description = "Shows youtube videos you've searched for.",
        options = [
            disnake.Option("search", "Video Search", disnake.OptionType.string, True),
            disnake.Option("amount", "Max Amount", disnake.OptionType.integer)
        ]
    )
    async def videosearch(inter, search:str, amount:int = 10):
        try:
            videos = extras.youtube_search(search, min(amount, 50))
            found_videos = ""
            for index, video in enumerate(videos):
                title = video["title"]
                link = video["link"]
                found_videos += f"{index + 1}: [{title}]({link})\n"
            embed = disnake.Embed(title = f"Results for {search}:", description = found_videos)
            await inter.send(embed = embed)
        except Exception:
            traceback.print_exc()

    @bot.slash_command(
        description = "Randomly finds a youtube video you've searched for.",
        options = [
            disnake.Option("search", "Video Search", disnake.OptionType.string, True),
            disnake.Option("amount", "Max Amount", disnake.OptionType.integer)
        ]
    )
    async def videofinder(inter, search:str, amount:int = 10):
        try:
            videos = extras.youtube_search(search, amount)
            await inter.send("Here's what I found when searching for " + search + ": " + random.choice(videos)["link"])
        except Exception:
            traceback.print_exc()

    @bot.slash_command(
        description = "Chat with a dumbass bot that can only say stuff randomly.",
        options = [
            disnake.Option("question", "Question", disnake.OptionType.string, True)
        ]
    )
    async def chat(inter, question:str):
        if question.lower().find("gay") != -1:
            await inter.send("Maybe")
            return
        elif question.lower().find("i run") != -1:
            await inter.send("START RUNNING NOW!")
            return
        elif question.lower().find("i die") != -1 or ((question.lower().find("not like") != -1 or question.lower().find("dislike") != -1 or question.lower().find("hate") != -1) and question.lower().find("yoy") != -1) or (question.lower().find("nsfw") != -1 and not (question.lower().find("not nsfw") != -1 or question.lower().find("no nsfw") != -1)):
            await inter.send("No")
            return
        elif question.lower().find("not die") != -1 or question.lower().find("not nsfw") != -1 or question.lower().find("no nsfw") != -1 or question.lower().find("yoy") != -1:
            await inter.send("Yes")
            return
        await inter.send(speach_types[hash(question.replace(" ", "")) % len(speach_types)].replace("$username", inter.author.tag))

    @bot.slash_command(
        description = "This is a mess!",
        options = [
            disnake.Option("length", "Length", disnake.OptionType.integer, True)
        ]
    )
    async def mess(inter, length:int):
        length = min(length, 2000)
        await inter.send(extras.unique_random_unicode(length))

    @bot.slash_command(
        description = "Totally not a jumpscare."
    )
    async def jumpscare(inter):
        await inter.send("Boo!")
        await asyncio.sleep(0.5)
        await inter.send(random.choice(jumpscares))

    @bot.slash_command()
    async def base64(inter):
        pass

    @base64.sub_command(
        description = "Encode Base64.",
        options = [
            disnake.Option("text", "Text", disnake.OptionType.string, True)
        ]
    )
    async def encode(inter, text:str):
        try:
            await inter.send(b64.b64encode(text.encode("UTF-8")).decode("UTF-8"))
        except Exception:
            await inter.send("Cannot encode the text.")

    @base64.sub_command(
        description = "Decode Base64.",
        options = [
            disnake.Option("text", "Text", disnake.OptionType.string, True)
        ]
    )
    async def decode(inter, text:str):
        try:
            await inter.send(b64.b64decode(text.encode("UTF-8")).decode("UTF-8"))
        except Exception:
            await inter.send("Cannot decode the text.")

    @bot.slash_command(
        description = "Helps with Research.",
        options = [
            disnake.Option("search", "Search", disnake.OptionType.string, True)
        ]
    )
    async def research(inter, search:str):
        await inter.send("Found Nothing, Please Try Again!")

    @bot.slash_command( 
        description = "Where is he actually?"
    )
    async def where(inter):
        await inter.send("Even tho bdidk235 is BruhKoli, bdidk235 doesn't like BruhKoli that much because he's used to bdidk235.")
        await inter.send("If you are intrested, This is bdidk235's Favorite Music Video: <https://www.youtube.com/watch?v=dQw4w9WgXcQ>!")
        await asyncio.sleep(2)
        await inter.send("bdidk235 unironically likes this song so don't get mad at him!")

    @bot.event
    async def on_message(message):
        if message.author.id == bot.user.id:
            return

        if bot.user.mentioned_in(message):
            if message.content == f"<@!{bot.user.id}>":
                await message.channel.send(random.choice(speach_types))
            else:
                question = message.content
                if question.lower().find("gay") != -1:
                    await message.channel.send("Maybe")
                    return
                elif question.lower().find("i run") != -1:
                    await message.channel.send("START RUNNING NOW!")
                    return
                elif question.lower().find("i die") != -1 or ((question.lower().find("not like") != -1 or question.lower().find("dislike") != -1 or question.lower().find("hate") != -1) and question.lower().find("yoy") != -1) or (question.lower().find("nsfw") != -1 and not (question.lower().find("not nsfw") != -1 or question.lower().find("no nsfw") != -1)):
                    await message.channel.send("No")
                    return
                elif question.lower().find("not die") != -1 or question.lower().find("not nsfw") != -1 or question.lower().find("no nsfw") != -1 or question.lower().find("yoy") != -1:
                    await message.channel.send("Yes")
                    return
                await message.channel.send(speach_types[hash(question.replace(f"<@!{bot.user.id}>", "").replace(" ", "")) % len(speach_types)].replace("$username", f"<@!{message.author.id}>"))

    @bot.event
    async def on_command_error(inter, error):
        if isinstance(error, commands.CommandOnCooldown):
            await inter.send(f"This command is on cooldown, you can use it again in {round(error.retry_after)} seconds.")

    @bot.event
    async def on_ready():
        print(f"{bot.user} is ready!")

    bot.run(token)

if __name__ == "__main__":
    main(str(os.environ.get("bot_token")))