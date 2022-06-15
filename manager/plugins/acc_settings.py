from manager import bot, LOG_GROUP
from telethon import events, Button
from manager.events import Cmd
from manager.database import DB
import re
import random

@Cmd(pattern="Accs Setting ⚙️")
async def acc_settings(event):
    ch_fname = "✅" if DB.get_key("CHANGE_ACCS_FNAME")[event.sender_id] == "yes" else "❌"
    ch_lname = "✅" if DB.get_key("CHANGE_ACCS_LNAME")[event.sender_id] == "yes" else "❌"
    ch_bio = "✅" if DB.get_key("CHANGE_ACCS_BIO")[event.sender_id] == "yes" else "❌"
    ch_uname = "✅" if DB.get_key("CHANGE_ACCS_USERNAME")[event.sender_id] == "yes" else "❌"
    ch_photo = "✅" if DB.get_key("CHANGE_ACCS_PHOTO")[event.sender_id] == "yes" else "❌"
    buttons = [
        [Button.inline(f"{ch_fname} Change FirstName {ch_fname}", data=f"ch_fname:{event.sender_id}")],
        [Button.inline(f"{ch_lname} Change LastName {ch_lname}", data=f"ch_lname:{event.sender_id}")],
        [Button.inline(f"{ch_bio} Change Bio {ch_bio}", data=f"ch_bio:{event.sender_id}")],
        [Button.inline(f"{ch_uname} Change Username {ch_uname}", data=f"ch_uname:{event.sender_id}")],
        [Button.inline(f"{ch_photo} Change Photo {ch_photo}", data=f"ch_photo:{event.sender_id}")],
    ]
    await event.reply(f"**• Welcome To Setting Panel For Your Accounts:**\n\n__• Edit Your Settings:__", buttons=buttons)

@bot.on(events.CallbackQuery(data=re.compile("ch\_(.*)\:(.*)")))
async def change_set(event):
    type = str(event.pattern_match.group(1).decode('utf-8'))
    id = str(event.pattern_match.group(2).decode('utf-8'))
    if type == "fname":
        all = DB.get_key("CHANGE_ACCS_FNAME")
        last = "no" if DB.get_key("CHANGE_ACCS_FNAME")[event.sender_id] == "yes" else "yes"
        all[event.sender_id] = last
        DB.set_key("CHANGE_ACCS_FNAME", all)
    ch_fname = "✅" if DB.get_key("CHANGE_ACCS_FNAME")[event.sender_id] == "yes" else "❌"
    ch_lname = "✅" if DB.get_key("CHANGE_ACCS_LNAME")[event.sender_id] == "yes" else "❌"
    ch_bio = "✅" if DB.get_key("CHANGE_ACCS_BIO")[event.sender_id] == "yes" else "❌"
    ch_uname = "✅" if DB.get_key("CHANGE_ACCS_USERNAME")[event.sender_id] == "yes" else "❌"
    ch_photo = "✅" if DB.get_key("CHANGE_ACCS_PHOTO")[event.sender_id] == "yes" else "❌"
    buttons = [
        [Button.inline(f"{ch_fname} Change FirstName {ch_fname}", data=f"ch_fname:{event.sender_id}")],
        [Button.inline(f"{ch_lname} Change LastName {ch_lname}", data=f"ch_lname:{event.sender_id}")],
        [Button.inline(f"{ch_bio} Change Bio {ch_bio}", data=f"ch_bio:{event.sender_id}")],
        [Button.inline(f"{ch_uname} Change Username {ch_uname}", data=f"ch_uname:{event.sender_id}")],
        [Button.inline(f"{ch_photo} Change Photo {ch_photo}", data=f"ch_photo:{event.sender_id}")],
    ]
    await event.edit(event, buttons=buttons)
