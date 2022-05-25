import os
os.system("pip install instagrapi")
os.system("pip install pillow")
from bomber import bot
from bomber.events import Cmd
import instaloader
import instagrapi
import re
import random

insta = instagrapi.Client()

@Cmd(pattern="/add")
async def add(event):
    insta.load_settings("bomber/session.json")
    media_id = insta.media_id(insta.media_pk_from_url("https://www.instagram.com/tv/CdxoYMhl_to/?igshid=YmMyMTA2M2Y="))
    edit = await event.edit("**• Starting . . .**")
    count = 0
    list = open("bomber/users.txt", "r").readlines()
    for i in range(1000):
        rand = random.choice(list)
        username = re.search("<Profile (.*) \((.*)\)>", rand)
        name = "@" + str(username[1])
        insta.media_comment(media_id, name)
        if (count % 10) == 0:
            await edit.edit(f"**• Added {count} Comment!**")
    await edit.edit("**• Completed!")
