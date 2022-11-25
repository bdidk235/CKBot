import os
import json
import random
import asyncio
import requests
import traceback
import base64 as b64
from enum import Enum
import dateutil.parser as dp
from disnake import *
from disnake.enums import *
from disnake.ext import commands
import extras

answers = {
    "bot": "I'm a bot made for Creatorkill because he's cool by bdidk235 mainly for the Generic RPG Server.",
    "bot_creation": "I'm made using Python with Disnake, You can also check out the [Source Code](https://github.com/bdidk235/CKBot) for this Bot.",
    "bdidk235": "bdidk235 is the developer of CKBot and also develops for the experience and other projects.",
    "creatorkill": "Creatorkill is a guy who does stuff and my name is based on his username because he's too cool to ignore.",
    "unby6": "unby6 is who Creatorkill used to be, but now just pretends creatorkill never existed!",
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
    OptionChoice("Who is unby6?", "unby6"),
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
    "You stupid.",
    "This is so ironic.",
    "Gamer",
    "Ok.",
    "Cancel it.",
    "You're Cancelled!",
    "What's 9 + 10?",
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
    bot = commands.Bot(intents = Intents(messages = True, message_content = True), command_prefix='$')

    @bot.slash_command(
        description = "Making as much of the Roblox API as possible!",
        options = [
            Option("data", "Data", OptionType.string, True, choices = [
                OptionChoice("User", "user"),
                OptionChoice("Experience", "experience"),
                OptionChoice("Group", "group"),
            ]),
            Option("id", "ID", OptionType.string, True)
        ]
    )
    async def roblox(
        inter: CommandInteraction,
        data: str,
        id: int
    ):
        print(f"{inter.author}: /roblox data: {data} id: {id}")
        await inter.response.defer()
        try:
            name = "Name"
            url = "https://roblox.com"
            icon_url = Embed.Empty
            info = "Info"
            if data == "user":
                if not id.strip().isdigit():
                    username = requests.post(f"https://users.roblox.com/v1/usernames/users", json={"usernames": [id]})
                    if username.status_code == 200:
                        id = username.json()["data"][0]["id"]
                    else:
                        await inter.send("Username cannot be found. If you're sure it exists, Try again later!", ephemeral = True)
                        return
                user = requests.get(f"https://users.roblox.com/v1/users/{id}")
                friend_count = requests.get(f"https://friends.roblox.com/v1/users/{id}/friends/count")
                username_history = requests.get(f"https://users.roblox.com/v1/users/{id}/username-history?limit=100")
                primary_role = requests.get(f"https://groups.roblox.com/v1/users/{id}/groups/primary/role")
                inventory_view = requests.get(f"https://inventory.roblox.com/v1/users/{id}/can-view-inventory")
                if user.status_code == 200:
                    user_data = user.json()
                    friend_count_data = friend_count.json() if friend_count.status_code == 200 else None
                    username_history_data = username_history.json()['data'] if username_history.status_code == 200 else None
                    primary_role_data = primary_role.json() if primary_role.content != None and primary_role.status_code == 200 else None
                    inventory_view_data = inventory_view.json() if inventory_view.status_code == 200 else None
                    badges = "[Verified] " if user_data['hasVerifiedBadge'] else ""\
                        + "[Banned] " if user_data['isBanned'] else ""
                    name = f"{badges}{user_data['displayName']} (@{user_data['name']})"
                    url = f"https://roblox.com/users/{id}/profile"
                    icon_url = f"https://www.roblox.com/headshot-thumbnail/image?userId={id}&width=420&height=420&format=png"
                    friends = ""
                    if friend_count_data:
                        friends = f"**Friends:** {friend_count_data['count']}\n"
                    public_inventory = ""
                    if inventory_view_data:
                        public_inventory = f"""\n**Public Inventory:** {"Yes" if inventory_view_data['canView'] else "No"}"""
                    primary_group = ""
                    if primary_role_data:
                        primary_group = f"""\n**Primary Group:** [{primary_role_data['group']['name']}](https://roblox.com/groups/{primary_role_data['group']['id']}/Group)
                        **Primary Group Role:** {primary_role_data['role']['name']}"""
                    previous_usernames = ""
                    if username_history_data and len(username_history_data) > 0:
                        previous_usernames = "\n\n**Previous Usernames:**\n"
                        for index, username in enumerate(username_history_data):
                            previous_usernames += f"{username['name']}"
                            if index != len(username_history_data) - 1:
                                previous_usernames += ", "
                    info = f"""**Description:**
                    ```{user_data['description'] if user_data['description'] and user_data['description'] != "" else " "}```
                    {friends}**Created:** <t:{int(dp.parse(user_data['created']).timestamp())}:R>{public_inventory}{primary_group}{previous_usernames}"""
                else:
                    await inter.send("Failed to load user data!", ephemeral = True)
                    return
            elif data == "experience":
                used_place_id = False
                place_id = 0
                if not id.strip().isdigit():
                    search = requests.get(f"https://games.roblox.com/v1/games/list?model.keyword={id}")
                    if search.status_code == 200:
                        id = search.json()["games"][0]["universeId"]
                    else:
                        await inter.send("An experience with that name cannot be found, Try again later!", ephemeral = True)
                        return
                else:
                    used_place_id = True
                    place_id = id
                    place_to_universe_id = requests.get(f"https://apis.roblox.com/universes/v1/places/{id}/universe")
                    if place_to_universe_id.status_code == 200:
                        id = place_to_universe_id.json()['universeId']
                    else:
                        await inter.send("Failed to get Universe ID from Place ID", ephemeral = True)
                        return
                universe = requests.get(f"https://games.roblox.com/v1/games?universeIds={id}")
                universe_places = requests.get(f"https://develop.roblox.com/v1/universes/{id}/places?limit=100")
                icon = requests.get(f"https://thumbnails.roblox.com/v1/games/icons?universeIds={id}&size=150x150&format=Png")
                if universe.status_code == 200:
                    universe_data = universe.json()['data'][0]
                    universe_places_data = universe_places.json()['data'] if universe_places.status_code == 200 else None
                    icon_data = icon.json()['data'][0] if icon.status_code == 200 else None
                    name = universe_data['name']
                    url = f"https://roblox.com/games/{universe_data['rootPlaceId']}/Game"
                    if icon_data and icon_data['state'] == "Completed":
                        icon_url = icon_data['imageUrl']
                    price = f"Price: {universe_data['price']}\n" if universe_data['price'] != None and universe_data['price'] > 0 else ""
                    avatarType = "Player Choice" if universe_data['universeAvatarType'] == "PlayerChoice" else\
                        "R15" if universe_data['universeAvatarType'] == "MorphToR15" else\
                        "R6" if universe_data['universeAvatarType'] == "MorphToR6" else ""
                    creator = ("[Verified] " if universe_data['creator']['hasVerifiedBadge'] else "") + (f"[@{universe_data['creator']['name']}](https://roblox.com/users/{universe_data['creator']['id']}/profile)\n" if universe_data['creator']['type'] == "User" else \
                        f"[{universe_data['creator']['name']}](https://roblox.com/groups/{universe_data['creator']['id']}/Group)\n" if universe_data['creator']['type'] == "Group" else "Unknown")
                    places = ""
                    if universe_places_data:
                        places = "\n\n**Places:**\n"
                        for place in universe_places_data:
                            places += f"[{place['name']}](https://roblox.com/games/{place['id']}/Game)\n"
                    gearsGenres = ""
                    if universe_data['allowedGearGenres'][0] != universe_data['genre']:
                        gearsGenres = "\n**Gears Genres:** "
                        for index, gear in enumerate(universe_data['allowedGearGenres']):
                            gearsGenres += f"{gear}"
                            if index != len(universe_data['allowedGearGenres']) - 1:
                                gearsGenres += ", "
                    gearsCategories = ""
                    if len(universe_data['allowedGearCategories']) > 0:
                        gearsCategories = "\n**Gears Categories:** "
                        for index, gear in enumerate(universe_data['allowedGearCategories']):
                            gearsGenres += f"{gear}"
                            if index != len(universe_data['allowedGearCategories']) - 1:
                                gearsGenres += ", "
                    info = f"""**By {creator}**
                    **Description:**
                    ```{universe_data['description'] if universe_data['description'] and universe_data['description'] != "" else " "}```
                    **Active:** {"{:,}".format(universe_data['playing'])}
                    **Favorites:** {"{:,}".format(universe_data['favoritedCount'])}
                    **Visits:** {"{:,}".format(universe_data['visits'])}
                    **Created:** <t:{int(dp.parse(universe_data['created']).timestamp())}:R>
                    **Last Updated:** <t:{int(dp.parse(universe_data['updated']).timestamp())}:R>
                    **Server Size:** {"{:,}".format(universe_data['maxPlayers'])}
                    **Genre:** {universe_data['genre']}{gearsGenres}{gearsCategories}

                    **Avatar Type:** {avatarType}
                    **Uncopylocked:** {"Yes" if universe_data['copyingAllowed'] else "No"}{places}"""
                else:
                    await inter.send("Failed to load universe data!", ephemeral = True)
                    return
            elif data == "group":
                if not id.strip().isdigit():
                    search = requests.get(f"https://groups.roblox.com/v1/groups/search/lookup?groupName={id}")
                    if search.status_code == 200:
                        id = search.json()["data"][0]["id"]
                    else:
                        await inter.send("A group with that name cannot be found, Try again later!", ephemeral = True)
                        return
                group = requests.get(f"https://groups.roblox.com/v1/groups/{id}")
                roles = requests.get(f"https://groups.roblox.com/v1/groups/{id}/roles")
                name_history = requests.get(f"https://groups.roblox.com/v1/groups/{id}/name-history?limit=100")
                icon = requests.get(f"https://thumbnails.roblox.com/v1/groups/icons?groupIds={id}&size=150x150&format=Png")
                if group.status_code == 200:
                    group_data = group.json()
                    roles_data = roles.json()['roles'] if roles.status_code == 200 else None
                    name_history_data = name_history.json()['data'] if name_history.status_code == 200 else None
                    icon_data = icon.json()['data'][0] if icon.status_code == 200 else None
                    name = ("[Verified] " if group_data['hasVerifiedBadge'] else "") + group_data['name']
                    url = f"https://roblox.com/groups/{id}/Group"
                    if icon_data and icon_data['state'] == "Completed":
                        icon_url = icon_data['imageUrl']
                    owner = "No One!"
                    if group_data.get('owner'):
                        owner = ("[Verified] " if group_data['owner']['hasVerifiedBadge'] else "") + f"[{group_data['owner']['displayName']} (@{group_data['owner']['username']})](https://roblox.com/users/{group_data['owner']['userId']}/profile)\n"
                    shout = ""
                    if group_data['shout']:
                        shout = f"\n**Shout:**\n```{group_data['shout']['body']}```" if group_data['shout']['body'] and group_data['shout']['body'] != "" else ""
                    locked = ""
                    if group_data.get('isLocked'):
                        locked = f"""\n**Locked:** {"Yes" if group_data['isLocked'] else "No"}"""
                    previous_names = ""
                    if name_history_data and len(name_history_data) > 0:
                        previous_names = "\n\n**Previous Usernames:**\n"
                        for index, name in enumerate(name_history_data):
                            previous_names += f"{name['name']}"
                            if index != len(name_history_data) - 1:
                                previous_names += ", "
                    roles = ""
                    if roles_data:
                        roles = "\n\n**Roles:**\n"
                        for role in roles_data:
                            if role['rank'] != 0 or role['memberCount'] != 0:
                                roles += f"{role['rank']}: {role['name']} ({role['memberCount']})\n"
                    info = f"""**By {owner}**
                    **Description:**
                    ```{group_data['description'] if group_data['description'] and group_data['description'] != "" else " "}```
                    **Members:** {group_data['memberCount']}
                    **Public:** {"Yes" if group_data['publicEntryAllowed'] else "No"}{locked}{shout}{previous_names}{roles}"""
                else:
                    await inter.send("Failed to load group data!", ephemeral = True)
                    return
            await inter.send(embed = Embed(description = info).set_author(name = name, url = url, icon_url = icon_url).set_footer(text = f"Provided by Roblox, ID: {id}"))
        except Exception:
            traceback.print_exc()

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
            await inter.send(embed = google_search_embed(search, amount))
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
            await inter.send(embed = youtube_search_embed(search, amount))
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
            await inter.send("Found Nothing, Please Try Again!", ephemeral = True)
            traceback.print_exc()

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
