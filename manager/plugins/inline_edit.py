from manager import bot, LOG_GROUP
from telethon import TelegramClient, events, Button
from telethon.sessions import StringSession
from manager.database import DB
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from faker import Faker
from . import main_menu, manage_menu
from manager.functions import search_photo
import re
import requests
import random

@bot.on(events.CallbackQuery(data=re.compile("yesedit\:(.*)")))
async def yesedit(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    session = DB.get_key("USER_ACCS")[event.sender_id][phone]
    client = TelegramClient(StringSession(session), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
    fake = Faker()
    if DB.get_key("CHANGE_ACCS_FNAME")[event.sender_id] == "yes":
        try:
            await client(UpdateProfileRequest(first_name=fake.first_name()))
        except:
            pass
    if DB.get_key("CHANGE_ACCS_LNAME")[event.sender_id] == "yes":
        try:
            await client(UpdateProfileRequest(last_name=fake.last_name()))
        except:
            pass
    if DB.get_key("CHANGE_ACCS_BIO")[event.sender_id] == "yes":
        try:
            await client(UpdateProfileRequest(about=fake.text().split(".")[0]))
        except:
            pass
    if DB.get_key("CHANGE_ACCS_USERNAME")[event.sender_id] == "yes":
        try:
            username = fake.first_name() + "_" + fake.last_name() + str(random.randint(100, 999))
            await client(UpdateUsernameRequest(username))
        except Exception as e:
            print(e)
            pass
    if DB.get_key("CHANGE_ACCS_PHOTO")[event.sender_id] == "yes":
        try:
            pics = search_photo(random.choice(["man", "woman", "boy", "girl"]))
            pic = random.choice(pics)
            img_data = requests.get(pic).content
            with open("photo.jpg", "wb") as handler:
                handler.write(img_data) 
            file = await client.upload_file("photo.jpg")
            await client(UploadProfilePhotoRequest(file=file))
            os.remove("photo.jpg")
        except Exception as e:
            print(e)
            pass
    await event.edit(f"**• Account Successfuly Edited And Manage Menu Send For You:**\n\n__• Dont Delete This Menu!__", buttons=main_menu)
    menu = manage_menu(phone)
    await event.reply(f"""
**#Manage_Menu**

**• Phone:** ( `{phone}` )

__• Dont Delete This Menu!__

**#Manage_Menu**
""", buttons=menu)
    

@bot.on(events.CallbackQuery(data=re.compile("noedit\:(.*)")))
async def noedit(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    await event.edit(f"**• Account Not Edited And Manage Menu Send For You:**\n\n__• Dont Delete This Menu!__", buttons=main_menu)
    menu = manage_menu(phone)
    await event.reply(f"""
**#Manage_Menu**

**• Phone:** ( `{phone}` )

__• Dont Delete This Menu!__

**#Manage_Menu**
""", buttons=menu)
