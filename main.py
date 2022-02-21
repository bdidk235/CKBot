import os
import asyncio
import disnake
import random
import traceback
from disnake.ext import commands
import extras

client = commands.Bot(sync_commands = True)
token = str(os.environ.get("bot_token"))

@client.slash_command(
    description = "Frequently Asked Questions!",
    options = [
        disnake.Option("question", "What is your question?", disnake.OptionType.string, True, choices = [
            disnake.OptionChoice("Why?", "why"),
            disnake.OptionChoice("What are you?", "bot"),
            disnake.OptionChoice("How are you made?", "bot_creation"),
            disnake.OptionChoice("Is There a Stealing Problem?", "stealing"),
            disnake.OptionChoice("Who is Creatorkill?", "creatorkill"),
            disnake.OptionChoice("What Admins do?", "admins"),
            disnake.OptionChoice("Yoy?", "yoy"),
        ])
    ]
)
async def faq(ctx, question: str):
    answers = {
        "why": "Why not?",
        "bot": "I'm a bot made for <@628260543588859904> because he's cool by <@622670618822967296> for the Generic RPG Game Server.",
        "bot_creation": "I'm made using Python with Disnake, You can also check out the [Source Code](https://github.com/bdidk235/CKBot) for this Bot.",
        "stealing": "Maybe? Hopefully not!",
        "creatorkill": "A guy who does stuff.",
        "admins": "Admins can do a lot of thing, and moderate the game they have access to admin commands and some other stuff.",
        "yoy": "yoy :smiley: :smiley: :smiley:"
    }
    await ctx.send(answers[question])

@client.slash_command(
    description = "Randomly Finds a Video Based on Your Search!",
    options = [
        disnake.Option("search", "Video Search", disnake.OptionType.string, True),
        disnake.Option("amount", "Amount of Possabilities", disnake.OptionType.integer)
    ]
)
async def videoSearch(ctx, search:str, amount:int = 10):
    try:
        videos = extras.youtube_search(search, amount)
        await ctx.send(random.choice(videos))
    except Exception:
        traceback.print_exc() 

@client.slash_command(
    description = "A Random Rickroll!",
    options = [
        disnake.Option("amount", "Amount of Possabilities", disnake.OptionType.integer)
    ]
)
async def rickroll(ctx, amount:int = 10):
    try:
        searches = ["rickroll", "never gonna give you up"]
        search = random.choice(searches)
        videos = extras.youtube_search(search, amount, True)
        await ctx.send(random.choice(videos))
    except Exception:
        traceback.print_exc() 

@client.event
async def on_ready():
    print(
        f"{client.user} is ready"
    )

client.run(token)
