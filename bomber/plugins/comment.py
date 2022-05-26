import os
os.system("pip install instagrapi")
os.system("pip install pillow")
from bomber import bot
from bomber.events import Cmd
from bomber.users import users
from telethon import events
import instagrapi
import re
import random
import asyncio
import requests

insta = instagrapi.Client()
insta.load_settings("bomber/session.json")
insta.login("mx_aboli", "imaboli83@#")

@bot.on(events.NewMessage(pattern="(?i)^\/add$", incoming=True, func=lambda e: e.is_private))
async def add(event):
    edit = await event.reply("**• Starting . . .**")
    media_id = insta.media_id(insta.media_pk_from_url("https://www.instagram.com/tv/CdxoYMhl_to"))
    count = 0
    while (True):
        rand = random.choice(users)
        username = re.search("<Profile (.*) \((.*)\)>", rand)
        name = "@" + str(username[1])
        try:
            r = requests.get("https://randomuser.me/api/").json()
            uname = r["results"][0]["login"]["username"]
            insta.media_comment(media_id, "@" + uname)
            count += 1
            await edit.edit(f"**• Added {count} Comment!**")
        except:
            pass
        await asyncio.sleep(3)
