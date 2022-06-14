from main import bot, LOG_GROUP
from telethon import TelegramClient
from manager.database import DB
from telethon.errors import (
    PhoneNumberInvalidError,
    PhoneNumberFloodError,
    PhoneNumberBannedError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError,
)
import random
import re
import os
import time
import requests
import glob

@bot.on_message(filters.private & filters.text & filters.regex("[\+]?[1-9][0-9 .\-\(\)]{8,16}[0-9]"))
async def add_account(client, message):
    edit1 = await message.reply("`• Please Wait . . .`")
    client = TelegramClient(f"sessions/{message.text}.session", 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
    try:
        scode = await client.send_code(message.text)
    except PhoneNumberInvalid:
        return await edit1.edit("**• Phone Number Is Invalid!**")
    except PhoneNumberFlood:
        return await edit1.edit("**• Phone Number Is Flooded!**")
    except PhoneNumberBanned:
        return await edit1.edit("**• Phone Number Is Banned!**")
    code = await bot.ask(message.chat.id, "**• Send Your Code:**", timeout=60)
    phone_code = code.text.replace(" ", "")
    edit2 = await message.reply("`• Please Wait . . .`")
    try:
        await client.sign_in(message.text, scode.phone_code_hash, phone_code)
    except PhoneCodeInvalid:
        return await edit2.edit("**• Your Code Is Invalid!**")
    except PhoneCodeExpired:
        return await edit2.edit("**• Your Code Is Expired!**")
    except SessionPasswordNeeded:
        await edit2.delete()
        edit3 = await message.reply("`• Please Wait . . .`")
        pas = await bot.ask(message.chat.id, "**• Send Your Password:**", timeout=60)           
        try:
            password = pas.text
            await client.check_password(password=password)
        except PasswordHashInvalidError:
            await bot.send_message(message.chat.id, "**• Your Password Is Invalid!**")
            return await bot.send_message(message.chat.id, "**• Please Send Your Number:**")
        await edit3.delete()
    await edit1.delete()
    await edit2.delete()
    sedit = await client.send_message("me", "`• Please Wait . . .`")
    edit4 = await message.reply("`• Please Wait . . .`")
    data = (requests.get("https://randomuser.me/api/").json())["results"][0]
    name = data["name"]
    bio = requests.get("https://api.codebazan.ir/bio/").text
    await client.update_profile(first_name=name["first"], last_name=name["last"], bio=bio)
    gender = "man" if data["gender"] == "male" else "woman"
    pics = photo(gender)
    for i in range(random.randint(3,10)):
        pic = random.choice(pics)
        img_data = requests.get(pic).content
        with open("photo.jpg", "wb") as handler:
            handler.write(img_data) 
        try:
            await client.set_profile_photo(photo="photo.jpg")
        except:
            pass
        os.remove("photo.jpg")
    try:
        await client.set_username(username=data["login"]["username"])
    except:
        pass
    try:
        await client.join_chat("durov")
        await client.join_chat("channel")
        await client.join_chat("video")
        await client.join_chat("Haebal_music")
        await client.join_chat("AndroidThemes")
        await client.join_chat("themes")
    except:
        pass
    await sedit.edit("**• Completed Edit Your Account!**")
    info = await client.get_me()
    await bot.send_message(LOG_GROUP, f"""
**#New_Acc**

**•| Account Info:**

 **• Number:** ( `{message.text}` )
 **• ID:** ( `{info.id}` )
 **• User:** ( @{info.username or "---"} )
 **• First Name:** ( `{info.first_name}` )
 **• Last Name:** ( `{info.last_name}` )
 **• Photo:** ( [Link]({pic}) )

**#New_Acc**
""")
    try:
        await client.log_out()
    except:
        pass
    await edit4.delete()
    await message.reply("**• Completed Edit Your Account!**")
