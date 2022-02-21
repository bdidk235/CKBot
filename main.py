import os
import asyncio
import disnake
from disnake.ext import commands
from extras import *

client = commands.Bot(sync_commands = True)
token = str(os.environ.get('bot_token'))

@client.slash_command(
    description="Frequently Asked Questions!",
    options=[
        disnake.Option("question", "What is your question?", disnake.OptionType.string, True, choices = [
            disnake.OptionChoice("What is this?", "faq"),
            disnake.OptionChoice("Who are you?", "bot"),
            disnake.OptionChoice("How are you made?", "bot_creation"),
            disnake.OptionChoice("What Admins do?", "admins"),
            disnake.OptionChoice("Yoy?", "yoy"),
        ])
    ]
)
async def faq(inter, question: str):
    answers = {
        "bot": "I'm a bot made for <@628260543588859904> because he's cool by <@622670618822967296> for the Generic RPG Game Server.",
        "bot_creation": "I'm made using python with disnake.",
        "faq": "I'm trying to answer your questions!",
        "admins": "Admins can do a lot of thing, and moderate the game they have access to admin commands and some other stuff.",
        "yoy": "yoy :smiley: :smiley: :smiley:"
    }
    await inter.send(answers[question])

@client.event
async def on_ready():
    print(
        f'{client.user} is ready'
    )

client.run(token)
