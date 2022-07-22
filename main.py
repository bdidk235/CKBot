import os
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

answers = {
    "bot": "I'm a bot made for Creatorkill because he's cool by bdidk235 mainly for the Generic RPG Server.",
    "bot_creation": "I'm made using Python with Disnake, You can also check out the [Source Code](https://github.com/bdidk235/CKBot) for this Bot.",
    "bdidk235": "bdidk235 is the developer of CKBot and also develops for the experience and other projects.",
    "creatorkill": "Creatorkill is a guy who does stuff and my name is based on his username because he's too cool to ignore.",
    "banana": "In Creatorkill's Basement.",
    "private": "You can use message me and I will still work with the commands.",
    "stealing": "Recently We have seen someone steal **air**, We will make sure to find who they are.",
    "like_me": "I like like you 🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫🤫",
    "stay_away": "Stay away from me!",
    "secret": "Don't let anyone know, Keep it a secret.",
}

faq_choices = [
    OptionChoice("What are you?", "bot"),
    OptionChoice("How are you made?", "bot_creation"),
    OptionChoice("Who is bdidk235?", "bdidk235"),
    OptionChoice("Who is Creatorkill?", "creatorkill"),
    OptionChoice("Where is the Banana?", "banana"),
    OptionChoice("Are you just an FAQ Bot?", "faq"),
    OptionChoice("Can I use you privately?", "private"),
    OptionChoice("Is There a Stealing Problem?", "stealing"),
    OptionChoice("Do you like me?", "like_me"),
    OptionChoice("I wanna do something bad!", "stay_away"),
    OptionChoice("I have a secret but I really wanna tell it!", "secret"),
]

speech_types = [
    "Yes",
    "No",
    "Maybe",
    "I'm not smart",
    "What you think you are?",
    "I met a person before!",
    "No. That's COMPLETELY WRONG!",
    "You are an idiot!",
    "Me",
    "I don't steal, I ask for it!",
    "I'm stupid",
    "This is so ironic.",
    "Gamer",
    "Ok.",
    "Cancel it.",
    "You're Cancelled!",
]

public_speech_types = [
    "WHERE IS $username, I CANT FIND THEM!",
    "$username PLEASE STOP!",
    "$username WHAT IS WRONG WITH YOU?",
    "hi $username :flushed:",
]

all_speech_types = speech_types + public_speech_types

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

def main(token):
    bot = commands.Bot(intents = Intents(messages = True, message_content = True), sync_commands = True)

    @bot.slash_command(
        description = "Frequently Asked questions.",
        options = [
            Option("question", "What is your question?", OptionType.string, True, choices = faq_choices)
        ]
    )
    async def faq(
        inter: CommandInteraction,
        question: str
    ):
        if question == "faq":
            await inter.send("I can also randomly rickroll you!", ephemeral = True)
            try:
                searches = ["rickroll", "rick roll", "never gonna give you up"]
                search = random.choice(searches)
                videos = extras.youtube_search(search, 25)
                await inter.send(random.choice(videos)["link"], ephemeral = True)
            except Exception:
                await inter.send("A Totally Random Rickroll: https://www.youtube.com/watch?v=dQw4w9WgXcQ", ephemeral = True)
                traceback.print_exc()
            return

        await inter.send(answers[question], ephemeral = True)

    @bot.slash_command(description = "yoy")
    async def yoy(inter: CommandInteraction):
        await inter.send("yoy <:yoy1:943929050097938453><:yoy2:943929050093748255>")

    @bot.slash_command(description = "gaem")
    async def gaem(inter: CommandInteraction):
        await inter.send("You epic gamer.")	

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
        print(f"{inter.author}: /research search: {search} amount: {amount}")
        await inter.response.defer()
        try:
            searches = googlesearch.search(search, min(amount, 25), advanced = True)
            found_searches = ""
            for index, gsearch in enumerate(searches):
                title = gsearch.title
                link = gsearch.url
                found_searches += f"{index + 1}: [{title}]({link})\n"
            embed = Embed(title = f"Results for {search}:", description = found_searches).set_footer(text = "Provided by Google")
            await inter.send(embed = embed)
        except Exception:
            await inter.send(content = "Found Nothing, Please Try Again!")
            traceback.print_exc()

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
        print(f"{inter.author}: /videosearch search: {search} amount: {amount}")
        await inter.response.defer()
        try:
            videos = extras.youtube_search(search, min(amount, 50))
            found_videos = ""
            for index, video in enumerate(videos):
                title = video["title"]
                link = video["link"]
                found_videos += f"{index + 1}: [{title}]({link})\n"
            embed = Embed(title = f"Results for {search}:", description = found_videos).set_footer(text = "Provided by YouTube")
            await inter.send(embed = embed)
        except Exception:
            await inter.send("Found Nothing, Please Try Again!")
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
        print(f"{inter.author}: /videofinder search: {search} amount: {amount}")
        await inter.response.defer()
        try:
            videos = extras.youtube_search(search, amount)
            link = random.choice(videos)["link"]
            await inter.send(f"Here's what I found when searching for {search}: {link}")
        except Exception:
            await inter.send("Found Nothing, Please Try Again!")
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
        await extras.respond(bot, inter, inter.author, question, command = True)

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

    @bot.slash_command(description = "Totally not a jumpscare.")
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
            await inter.send("Cannot encode the text.", ephemeral = True)

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
            await inter.send("Cannot decode the text.", ephemeral = True)

    @bot.message_command(name = "Base64 Encode")
    async def message_b64_encode(inter: ApplicationCommandInteraction, message: Message):
        text = message.content
        try:
            await inter.send(b64.b64encode(text.encode("UTF-8")).decode("UTF-8"))
        except Exception:
            await inter.send("Cannot encode the text.", ephemeral = True)

    @bot.message_command(name = "Base64 Decode")
    async def message_b64_decode(inter: ApplicationCommandInteraction, message: Message):
        text = message.content
        try:
            await inter.send(b64.b64decode(text.encode("UTF-8")).decode("UTF-8"))
        except Exception:
            await inter.send("Cannot encode the text.", ephemeral = True)

    @bot.event
    async def on_message(message: Message):
        if message.author.id == bot.user.id:
            return

        if bot.user.mentioned_in(message) or (private := message.channel.type == ChannelType.private):
            if message.content == f"<@!{bot.user.id}>":
                speech_type = main.speech_types if private else main.all_speech_types
                await message.channel.send(random.choice(speech_type))
            else:
                await asyncio.sleep(0.8)
                await extras.respond(bot, message.channel, message.author, message.content, private)

    @bot.event
    async def on_command_error(
        inter: Interaction,
        exception: Exception
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
