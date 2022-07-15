import main
import random
import asyncio
from youtubesearchpython import SearchVideos
from disnake import *
from disnake.ext import commands

def get_name_from_faq(question: str):
    lower_choices = [OptionChoice(answer.name.lower(), answer.value) for answer in main.faq_choices]
    answers = [i for i, o in enumerate(lower_choices) if o.name == question.lower()]

    if answers != []:
        return answers[0]

def get_answer_from_faq(faq: str):
    if answer := get_name_from_faq(faq):
        return main.answers[main.faq_choices[answer].value]

def unique_random_unicode(length):
    random_ints = random.sample(range(0x07FF), length)
    random_unicodes = [chr(x) for x in random_ints]
    return u"".join(random_unicodes)

def youtube_search(search, max_results:int = 10):
    return [video for video in SearchVideos(search, mode = "dict", max_results = max_results).result()['search_result']]

async def respond(bot: commands.Bot, re: Interaction, author, question: str, private: bool = False, command: bool = False):
    print(f"{author}: {question} (DM: {private})")
    speech_type = main.speech_types if private else main.all_speech_types
    response = None
    if not command and question.startswith("/"):
        response = "Failed commmand <:imagine:997168475594301490>"
    elif question.lower() == "about me":
        await re.send("First Of All")
        await asyncio.sleep(1)
        await re.send("I'm gonna assume that you are a **human**")
        await asyncio.sleep(2)
        await re.send("I hope you have good job and stuff, I guess?")
        return
    elif question.lower() == "are you just an faq bot?" or question.lower() == "are you just a faq bot?":
        await re.send("I can also randomly rickroll you!")
        try:
            searches = ["rickroll", "rick roll", "never gonna give you up"]
            search = random.choice(searches)
            videos = youtube_search(search, 25)
            await re.send(random.choice(videos)["link"])
        except Exception:
            await re.send("A Totally Random Rickroll: https://www.youtube.com/watch?v=dQw4w9WgXcQ")
            traceback.print_exc()
        return
    elif faq := get_answer_from_faq(question):
        response = faq
    elif question.lower().find("gay") != -1:
        response = "<:chillbob:964329423232991282>"
    elif question.lower().find("i run") != -1:
        response = "START RUNNING NOW!"
    elif question.lower().find("i die") != -1 or ((question.lower().find("not like") != -1 or question.lower().find("dislike") != -1 or question.lower().find("hate") != -1) and question.lower().find("yoy") != -1) or (question.lower().find("nsfw") != -1 and not (question.lower().find("not nsfw") != -1 or question.lower().find("no nsfw") != -1)):
        response = "No"
    elif question.lower().find("not die") != -1 or question.lower().find("not nsfw") != -1 or question.lower().find("no nsfw") != -1 or question.lower().find("yoy") != -1:
        response = "Yes"
    else:
        response = speech_type[hash(question.lower().replace(f"<@!{bot.user.id}>", "").replace(" ", "")) % len(speech_type)].replace("$username", f"<@!{author.id}>")
    await re.send(response)
