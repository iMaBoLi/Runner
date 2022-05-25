import os
os.system("pip install instaloader")
os.system("pip install instagrapi")
import instaloader
import instagrapi
import re
import random

insta = instaloader.Instaloader()
insta.login("mx_aboli", "abol83@#")       
profile = instaloader.Profile.from_username(insta.context, "bahman_japoni")
list = []
fols = profile.get_followers()
for x in fols:
    list.append(str(x))

insta = instagrapi.Client()
insta.load_settings("session.json")

media_id = insta.media_id(insta.media_pk_from_url("https://www.instagram.com/tv/CdxoYMhl_to/?igshid=YmMyMTA2M2Y="))

for i in range(1000):
    rand = random.choice(list)
    username = re.search("<Profile (.*) \((.*)\)>", rand)
    name = "@" + str(username[1])
    insta.media_comment(media_id, name)
