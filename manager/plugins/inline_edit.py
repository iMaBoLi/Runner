from manager import bot, LOG_GROUP
from telethon import TelegramClient, events, Button
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.photos import UpdateProfilePhotoRequest
from faker import Faker
from manager.functions import search_photo, create_file, delete_file
import re
import random

@bot.on(events.CallbackQuery(data=re.compile("yesedit\:(.*)")))
async def yesedit(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    manage_menu = [
        [Button.inline("• LogOut •", data=f"logout:{phone}")],
        [Button.inline("• Reset Authorization •", data=f"resetauthorization:{phone}")],
        [Button.inline("• Receive Codes •", data=f"getcodes:{phone}")],
    ]
    client = TelegramClient(f"sessions/{phone}.session", 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
    fake = Faker()
    try:
        await client(UpdateProfileRequest(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            about=fake.text().split(".")[0],
        ))
    except Exception as e:
        print(e)
        pass
    try:
        pics = search_photo(random.choice(["man", "woman", "boy", "girl"]))
        for i in range(random.randint(3,8)):
            pic = random.choice(pics)
            img_data = requests.get(pic).content
            with open("photo.jpg", "wb") as handler:
                handler.write(img_data) 
            try:
                file = await client.upload_file("photo.jpg")
                await client(UploadProfilePhotoRequest(file=file))
            except:
                pass
            os.remove("photo.jpg")
    except Exception as e:
        print(e)
        pass
    delete_file(f"sessions/{phone}.session")
    create_file(f"sessions/{phone}.session", f"sessions/{phone}.session")
    await event.edit(f"**• Accoutn Successfuly Edited And Manage Menu Send For You:**\n\n__• Dont Delete This Menu!__")
    await event.reply(f"""
**#Manage_Menu**

**• Phone:** ( `{phone}` )

__• Dont Delete This Menu!__

**#Manage_Menu**
""", buttons=manage_menu)
    

@bot.on(events.CallbackQuery(data=re.compile("noedit\:(.*)")))
async def yesedit(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    manage_menu = [
        [Button.inline("• LogOut •", data=f"logout:{phone}")],
        [Button.inline("• Reset Authorization •", data=f"resetauthorization:{phone}")],
        [Button.inline("• Receive Codes •", data=f"getcodes:{phone}")],
    ]
    delete_file(f"sessions/{phone}.session")
    create_file(f"sessions/{phone}.session", f"sessions/{phone}.session")
    await event.edit(f"**• Accoutn Not Edited And Manage Menu Send For You:**\n\n__• Dont Delete This Menu!__")
    await event.reply(f"""
**#Manage_Menu**

**• Phone:** ( `{phone}` )

__• Dont Delete This Menu!__

**#Manage_Menu**
""", buttons=manage_menu)
