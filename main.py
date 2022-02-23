import os
import json
import asyncio
import disnake
import random
import requests
import traceback
from enum import Enum
from disnake.enums import *
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
                disnake.OptionChoice("Who is BruhKoli?", "bruhkoli"),
                disnake.OptionChoice("Are you just an FAQ Bot?", "faq"),
                disnake.OptionChoice("Can I use you privately?", "private"),
                
                disnake.OptionChoice("Is There a Stealing Problem?", "stealing"),
                disnake.OptionChoice("Who is Amogus?", "amogus"),
                disnake.OptionChoice("Who is Creatorkill?", "creatorkill"),
                disnake.OptionChoice("What Admins do?", "admins"),
                disnake.OptionChoice("What does Bobo Mean?", "bobo"),
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
                searches = ["rickroll", "rick roll", "never gonna give you up"]
                search = random.choice(searches)
                videos = extras.youtube_search(search, 25)
                await ctx.send(random.choice(videos)["link"])
            except Exception:
                traceback.print_exc()
            return

        answers = {
            "bot": "I'm a bot made for Creatorkill because he's cool by BruhKoli mainly for the Generic RPG Game Server.",
            "bot_creation": "I'm made using Python with Disnake, You can also check out the [Source Code](https://github.com/bdidk235/CKBot) for this Bot.",
            "bruhkoli": "BruhKoli is the developer of CKBot and also develops for the game and other projects.",
            "private": "You can use message me and I will still work with the commands.",
            "stealing": "Maybe? Hopefully not!",
            "amogus": "Amogus a.k.a. KonradRon2 is the Owner of Generic RPG Game.",
            "creatorkill": "Creatorkill is a guy who does stuff and my name is based on his username because he's too cool to ignore.",
            "admins": "Admins can do a lot of thing, and moderate the game they have access to admin commands and some other stuff.",
            "bobo": "Bobo :rofl:",
            "suck": "It's not a rickroll, Trust me! https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            "suck2": "You suck at using me, You couldn't have scrolled down here!",
            "idiot": "You are probably The REAL Idiot or but maybe I am...",
            "why": "Why not?",
        }
        await ctx.send(answers[question])

    @client.slash_command(
        description = "yoy"
    )
    async def yoy(ctx):
        await ctx.send("yoy <:yoy1:943929050097938453><:yoy2:943929050093748255>")

    @client.slash_command(
        description = "Shows youtube videos you've searched for.",
        options = [
            disnake.Option("search", "Video Search", disnake.OptionType.string, True),
            disnake.Option("amount", "Max Amount of Videos", disnake.OptionType.integer)
        ]
    )
    async def videosearch(ctx, search:str, amount:int = 10):
        try:
            videos = extras.youtube_search(search, min(amount, 50))
            found_videos = ""
            for index, video in enumerate(videos):
                title = video["title"]
                link = video["link"]
                found_videos += f"{index + 1}: [{title}]({link})\n"
            embed = disnake.Embed(title = f"Results for {search}:", description = found_videos)
            await ctx.send(embed = embed)
        except Exception:
            traceback.print_exc()

    @client.slash_command(
        description = "Randomly find a youtube video you've searched for.",
        options = [
            disnake.Option("search", "Video Search", disnake.OptionType.string, True),
            disnake.Option("amount", "Max Amount of Possible Videos", disnake.OptionType.integer)
        ]
    )
    async def videofinder(ctx, search:str, amount:int = 10):
        try:
            videos = extras.youtube_search(search, amount)
            await ctx.send("Here's what I found when searching " + search + ": " + random.choice(videos)["link"])
        except Exception:
            traceback.print_exc()

    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown, you can use it again in {round(error.retry_after)} seconds.")

    @client.event
    async def on_ready():
        print(f"{client.user} is ready!")

    client.run(token)

if __name__ == "__main__":
    main(str(os.environ.get("bot_token")))