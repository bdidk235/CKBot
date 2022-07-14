import main
import random
from youtubesearchpython import SearchVideos
from disnake import *
from disnake.ext import commands

async def respond(bot: commands.Bot, re: Interaction, author, question: str, private: bool = False):
    speech_type = main.all_speech_types
    if private:
        speech_type = main.speech_types
    response = None
    if question.lower().find("gay") != -1:
        response = "<:chillbob:964329423232991282>"
    elif question.lower().find("i run") != -1:
        response = "START RUNNING NOW!"
    elif question.lower().find("i die") != -1 or ((question.lower().find("not like") != -1 or question.lower().find("dislike") != -1 or question.lower().find("hate") != -1) and question.lower().find("yoy") != -1) or (question.lower().find("nsfw") != -1 and not (question.lower().find("not nsfw") != -1 or question.lower().find("no nsfw") != -1)):
        response = "No"
    elif question.lower().find("not die") != -1 or question.lower().find("not nsfw") != -1 or question.lower().find("no nsfw") != -1 or question.lower().find("yoy") != -1:
        response = "Yes"
    else:
        response = speech_type[hash(question.lower().replace(f"<@!{bot.user.id}>", "").replace(" ", "")) % len(speech_type)].replace("$username", f"<@!{author.id}>")
    print(f"{author}: {question} (DM: {private})")
    await re.send(response)

def unique_random_unicode(length):
    random_ints = random.sample(range(0x07FF), length)
    random_unicodes = [chr(x) for x in random_ints]
    return u"".join(random_unicodes)

def youtube_search(search, max_results:int = 10):
    return [video for video in SearchVideos(search, mode = "dict", max_results = max_results).result()['search_result']]