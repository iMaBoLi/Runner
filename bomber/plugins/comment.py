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
insta.login("mx_aboli", "abol83@#")

@bot.on(events.NewMessage(pattern="(?i)^\/add$", incoming=True, func=lambda e: e.is_private))
async def add(event):
    edit = await event.reply("**• Starting . . .**")
    media_id = insta.media_id(insta.media_pk_from_url("https://www.instagram.com/tv/CdxoYMhl_to/?igshid=YmMyMTA2M2Y="))
    list = users
    for i in range(1000):
        rand = random.choice(list)
        username = re.search("<Profile (.*) \((.*)\)>", rand)
        name = "@" + str(username[1])
        insta.media_comment(media_id, name)
        try:
            await edit.edit(f"**• Added {i} Comment!**")
        except:
            pass
    await edit.edit("**• Completed!")
