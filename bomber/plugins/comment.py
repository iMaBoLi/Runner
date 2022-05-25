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

insta = instagrapi.Client()
insta.login("zxaboli83", "abol83@#")

@bot.on(events.NewMessage(pattern="(?i)^\/add$", incoming=True, func=lambda e: e.is_private))
async def add(event):
    edit = await event.reply("**• Starting . . .**")
    media_id = insta.media_id(insta.media_pk_from_url("https://www.instagram.com/tv/CdxoYMhl_to"))
    count = 1
    while (True):
        rand = random.choice(users)
        username = re.search("<Profile (.*) \((.*)\)>", rand)
        name = "@" + str(username[1])
        try:
            com = insta.media_comment(media_id, name)
            count += 1
        except:
            pass
        try:
            await edit.edit(f"**• Added {count} Comment!**")
        except:
            print(f"**• Added {count} Comment!**")
