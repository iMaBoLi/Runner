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
insta.set_user_agent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36")

@bot.on(events.NewMessage(pattern="(?i)^\/add$", incoming=True, func=lambda e: e.is_private))
async def add(event):
    edit = await event.reply("**• Starting . . .**")
    media_id = "2842230424423889768_5679860007"
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
