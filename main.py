import os
import asyncio
import disnake
import random
import traceback
from disnake.ext import commands
import extras

def main(token):
    client = commands.Bot(sync_commands = True)

    @client.slash_command(
        description = "Frequently Asked questions.",
        options = [
            disnake.Option("question", "What is your question?", disnake.OptionType.string, True, choices = [
                disnake.OptionChoice("What are you?", "bot"),
                disnake.OptionChoice("How are you made?", "bot_creation"),
                disnake.OptionChoice("Are you just an FAQ Bot?", "faq"),
                disnake.OptionChoice("Can I use you privately?", "private"),
                disnake.OptionChoice("Is There a Stealing Problem?", "stealing"),
                disnake.OptionChoice("Who is Creatorkill?", "creatorkill"),
                disnake.OptionChoice("What Admins do?", "admins"),
                disnake.OptionChoice("Yoy?", "yoy"),
                disnake.OptionChoice("Do You Suck at everything?", "suck"),
                disnake.OptionChoice("Do You Suck at something?", "suck2"),
                disnake.OptionChoice("Are you an Idiot?", "idiot"),
                disnake.OptionChoice("Why?", "why"),
            ])
        ]
    )
    async def faq(ctx, question: str):
        if question == "faq":
            await ctx.send("I can also randomly rickroll you!")
            try:
                searches = ["rickroll", "never gonna give you up"]
                search = random.choice(searches)
                videos = extras.youtube_search(search, 10, True)
                await ctx.send(random.choice(videos))
            except Exception:
                traceback.print_exc()
            return 

        answers = {
            "bot": "I'm a bot made for <@628260543588859904> because he's cool by <@622670618822967296> for the Generic RPG Game Server.",
            "bot_creation": "I'm made using Python with Disnake, You can also check out the [Source Code](https://github.com/bdidk235/CKBot) for this Bot.",
            "private": "You can use message me and I will still work with the commands.",
            "stealing": "Maybe? Hopefully not!",
            "creatorkill": "A guy who does stuff.",
            "admins": "Admins can do a lot of thing, and moderate the game they have access to admin commands and some other stuff.",
            "yoy": "yoy :smiley: :smiley: :smiley:",
            "suck": "It's not a rickroll, Trust me! https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "suck2": "You suck at using me, You couldn't have scrolled down here!",
            "idiot": "You are probably The REAL Idiot or but maybe I am...",
            "why": "Why not?",
        }
        await ctx.send(answers[question])

    @client.slash_command(
        description = "Randomly finds a video on your search.",
        options = [
            disnake.Option("search", "Video Search", disnake.OptionType.string, True),
            disnake.Option("amount", "Amount of Possabilities", disnake.OptionType.integer)
        ]
    )
    async def videosearch(ctx, search:str, amount:int = 10):
        try:
            videos = extras.youtube_search(search, amount)
            await ctx.send(random.choice(videos))
        except Exception:
            traceback.print_exc() 

    @client.slash_command(
        description = "A random rickroll.",
        options = [
            disnake.Option("amount", "Amount of Possabilities", disnake.OptionType.integer)
        ]
    )
    async def rickroll(ctx, amount:int = 10):
        try:
            searches = ["rickroll", "never gonna give you up"]
            search = random.choice(searches)
            videos = extras.youtube_search(search, amount)
            await ctx.send(random.choice(videos))
        except Exception:
            traceback.print_exc() 

    @client.event
    async def on_ready():
        print(
            f"{client.user} is ready!"
        )

    client.run(token)

if __name__ == "__main__":
    main(str(os.environ.get("bot_token")))