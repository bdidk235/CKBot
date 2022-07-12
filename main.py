import os
import json
import string
import random
import asyncio
import traceback
import googlesearch
import base64 as b64
from enum import Enum
from disnake import *
from disnake.enums import *
from disnake.ext import commands
import extras

def main(token):
    bot = commands.Bot(command_prefix = commands.when_mentioned, sync_commands = True)

    answers = {
        "bot": "I'm a bot made for Creatorkill because he's cool by bdidk235 mainly for the Generic RPG Server.",
        "bot_creation": "I'm made using Python with Disnake, You can also check out the [Source Code](https://github.com/bdidk235/CKBot) for this Bot.",
        "bdidk235": "bdidk235 is the developer of CKBot and also develops for the experience and other projects.",
        "creatorkill": "Creatorkill is a guy who does stuff and my name is based on his username because he's too cool to ignore.",
        "banana": "In Creatorkill's Basement.",
        "private": "You can use message me and I will still work with the commands.",
        "stealing": "Maybe? Hopefully not!",
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
            Option("question", "What is your question?", OptionType.string, True, choices = [
                OptionChoice("What are you?", "bot"),
                OptionChoice("How are you made?", "bot_creation"),
                OptionChoice("Who is bdidk235?", "bdidk235"),
                OptionChoice("Who is Creatorkill?", "creatorkill"),
                OptionChoice("Where is the Banana?", "banana"),
                OptionChoice("Are you just an FAQ Bot?", "faq"),
                OptionChoice("Can I use you privately?", "private"),
                OptionChoice("Is There a Stealing Problem?", "stealing"),
            ])
        ]
    )
    async def faq(
        inter: CommandInteraction,
        question: str
    ):
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
    async def yoy(inter: CommandInteraction):
        await inter.send("yoy <:yoy1:943929050097938453><:yoy2:943929050093748255>")

    @bot.slash_command(
        description = "Shows youtube videos you've searched for.",
        options = [
            Option("search", "Video Search", OptionType.string, True),
            Option("amount", "Max Amount", OptionType.integer)
        ]
    )
    async def videosearch(
        inter: CommandInteraction,
        search:str,
        amount:int = 10
    ):
        try:
            videos = extras.youtube_search(search, min(amount, 50))
            found_videos = ""
            for index, video in enumerate(videos):
                title = video["title"]
                link = video["link"]
                found_videos += f"{index + 1}: [{title}]({link})\n"
            embed = Embed(title = f"Results for {search}:", description = found_videos)
            await inter.send(embed = embed)
        except Exception:
            traceback.print_exc()

    @bot.slash_command(
        description = "Randomly finds a youtube video you've searched for.",
        options = [
            Option("search", "Video Search", OptionType.string, True),
            Option("amount", "Max Amount", OptionType.integer)
        ]
    )
    async def videofinder(
        inter: CommandInteraction,
        search: str,
        amount: int = 10
    ):
        try:
            videos = extras.youtube_search(search, amount)
            await inter.send("Here's what I found when searching for " + search + ": " + random.choice(videos)["link"])
        except Exception:
            traceback.print_exc()

    @bot.slash_command(
        description = "Chat with a dumbass bot that can only say stuff randomly.",
        options = [
            Option("question", "Question", OptionType.string, True)
        ]
    )
    async def chat(
        inter: CommandInteraction,
        question: str
    ):
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
        await inter.send(speach_types[hash(question.replace(" ", "")) % len(speach_types)].replace("$username", f"<@{inter.author.id}>"))

    @bot.slash_command(
        description = "This is a mess!",
        options = [
            Option("length", "Length", OptionType.integer, True)
        ]
    )
    async def mess(
        inter: CommandInteraction,
        length: int
    ):
        length = min(length, 2000)
        await inter.send(extras.unique_random_unicode(length))

    @bot.slash_command(
        description = "Totally not a jumpscare."
    )
    async def jumpscare(inter: CommandInteraction):
        await inter.send("Boo!")
        await asyncio.sleep(0.25)
        await inter.send(random.choice(jumpscares))

    @bot.slash_command()
    async def base64(inter: CommandInteraction):
        pass

    @base64.sub_command(
        name = "encode",
        description = "Encode Base64.",
        options = [
            Option("text", "Text", OptionType.string, True)
        ]
    )
    async def b64_encode(
        inter: CommandInteraction,
        text: str
    ):
        try:
            await inter.send(b64.b64encode(text.encode("UTF-8")).decode("UTF-8"))
        except Exception:
            await inter.send("Cannot encode the text.")

    @base64.sub_command(
        name = "decode",
        description = "Decode Base64.",
        options = [
            Option("text", "Text", OptionType.string, True)
        ]
    )
    async def b64_decode(
        inter: CommandInteraction,
        text: str
    ):
        try:
            await inter.send(b64.b64decode(text.encode("UTF-8")).decode("UTF-8"))
        except Exception:
            await inter.send("Cannot decode the text.")

    @bot.message_command(name = "Base64 Encode")
    async def message_b64_encode(inter: ApplicationCommandInteraction, message: Message):
        text = message.content[::-1]
        try:
            await inter.response.send_message(b64.b64encode(text.encode("UTF-8")).decode("UTF-8"))
        except Exception:
            await inter.response.send_message("Cannot encode the text.")
    @bot.message_command(name = "Base64 Decode")
    async def message_b64_decode(inter: ApplicationCommandInteraction, message: Message):
        text = message.content[::-1]
        try:
            await inter.response.send_message(b64.b64decode(text.encode("UTF-8")).decode("UTF-8"))
        except Exception:
            await inter.response.send_message("Cannot encode the text.")

    @bot.slash_command(
        description = "Helps with Research.",
        options = [
            Option("search", "Search", OptionType.string, True),
            Option("amount", "Max Amount", OptionType.integer)
        ]
    )
    async def research(
        inter: CommandInteraction,
        search: str,
        amount: int = 10
    ):
        try:
            searches = googlesearch.search(search, min(amount, 25), advanced = True)
            found_searches = ""
            for index, gsearch in enumerate(searches):
                title = gsearch.title
                link = gsearch.url
                found_searches += f"{index + 1}: [{title}]({link})\n"
            embed = Embed(title = f"Results for {search}:", description = found_searches)
            await inter.send(embed = embed)
        except Exception:
            await inter.send("Found Nothing, Please Try Again!")
            traceback.print_exc()

    @bot.slash_command( 
        description = "Where is he actually?"
    )
    async def where(inter: CommandInteraction):
        await inter.send("Even tho bdidk235 is BruhKoli, bdidk235 doesn't like BruhKoli that much because he's used to bdidk235.")
        await inter.send("If you are intrested, This is bdidk235's Favorite Music Video: <https://www.youtube.com/watch?v=dQw4w9WgXcQ>!")
        await asyncio.sleep(2)
        await inter.send("bdidk235 unironically likes this song so don't get mad at him!")

    @bot.event
    async def on_message(message: Message):
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
    async def on_command_error(
        inter,
        exception
    ):
        if isinstance(exception, commands.CommandOnCooldown):
            await inter.send(f"This command is on cooldown, you can use it again in {round(exception.retry_after)} seconds.")

    @bot.event
    async def on_ready():
        await bot.change_presence(activity = Game(name = "Untitled Server Game"))
        print(f"{bot.user} is ready!")

    bot.run(token)

if __name__ == "__main__":
    main(str(os.environ.get("bot_token")))
