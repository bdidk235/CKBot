import random
import googlesearch
import youtubesearchpython
from disnake import *
from disnake.ext import commands

def unique_random_unicode(length: int):
    random_ints = random.sample(range(0x07FF), length)
    random_unicodes = [chr(x) for x in random_ints]
    return u"".join(random_unicodes)

def google_search_embed(search: str, max_results: int = 10):
    searches = googlesearch.search(search, min(amount, 25), advanced = True)
    found_searches = ""
    for index, gsearch in enumerate(searches):
        title = gsearch.title
        link = gsearch.url
        found_searches += f"{index + 1}: [{title}]({link})\n"
    return Embed(title = f"Results for {search}:", description = found_searches).set_footer(text = "Provided by Google")

def youtube_search(search: str, max_results: int = 10):
    return [video for video in youtubesearchpython.SearchVideos(search, mode = "dict", max_results = max_results).result()['search_result']]

def youtube_search_embed(search: str, max_results: int = 10):
    videos = youtube_search(search, min(amount, 50))
    found_videos = ""
    for index, video in enumerate(videos):
        title = video["title"]
        link = video["link"]
        found_videos += f"{index + 1}: [{title}]({link})\n"
    return Embed(title = f"Results for {search}:", description = found_videos).set_footer(text = "Provided by YouTube")