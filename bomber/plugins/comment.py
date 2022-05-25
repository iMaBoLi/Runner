import os
os.system("pip install instaloader")
os.system("pip install instagrapi")
os.system("pip install pillow")
import instaloader
import instagrapi
import re
import random

insta = instaloader.Instaloader()
insta.login("mx_aboli", "abol83@#")       
profile = instaloader.Profile.from_username(insta.context, "sheykh_apex")
list = []
fols = profile.get_followers()
for x in fols:
    list.append(str(x))

insta = instagrapi.Client()
insta.load_settings("session.json")
media_id = insta.media_id(insta.media_pk_from_url("https://www.instagram.com/tv/CdxoYMhl_to/?igshid=YmMyMTA2M2Y="))

from bomber import bot
from bomber.events import Cmd

@Cmd(pattern="/add")
async def add(event):
    edit = await event.edit("**• Starting . . .**")
    count = 0
    for i in range(1000):
        rand = random.choice(list)
        username = re.search("<Profile (.*) \((.*)\)>", rand)
        name = "@" + str(username[1])
        insta.media_comment(media_id, name)
        if (count % 10) == 0:
            await edit.edit(f"**• Added {count} Comment!**")
    await edit.edit("**• Completed!")
