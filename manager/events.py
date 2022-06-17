from . import bot, LOG_GROUP, CHANNEL
from telethon import events, functions, Button
from manager.database import DB
from traceback import format_exc
from manager.plugins import main_menu
import os
import sys
import re
import asyncio
        
def Cmd(
    pattern=None,
    admin_only=False,
    **kwargs,
):
    def decorator(func):
        async def wrapper(event):

            BOT_USERS = DB.get_key("BOT_USERS") or []
            if event.sender_id not in BOT_USERS:
                BOT_USERS.append(event.sender_id)
                DB.set_key("BOT_USERS", BOT_USERS)
                await bot.send_message(LOG_GROUP, f"**#New_User**\n\n**• UserID:** ( `{event.sender_id}` )")

            USER_ACCS_COUNT = DB.get_key("USER_ACCS_COUNT") or {}
            if event.sender_id not in USER_ACCS_COUNT:                 
                USER_ACCS_COUNT.update({event.sender_id: 0})
                DB.set_key("USER_ACCS_COUNT", USER_ACCS_COUNT)

            USER_ACCS = DB.get_key("USER_ACCS") or {}
            if event.sender_id not in USER_ACCS:                 
                USER_ACCS.update({event.sender_id: {}})
                DB.set_key("USER_ACCS", USER_ACCS)

            CHANGE_ACCS_FNAME = DB.get_key("CHANGE_ACCS_FNAME") or {}
            if event.sender_id not in CHANGE_ACCS_FNAME:                 
                CHANGE_ACCS_FNAME.update({event.sender_id: "yes"})
                DB.set_key("CHANGE_ACCS_FNAME", CHANGE_ACCS_FNAME)

            CHANGE_ACCS_LNAME = DB.get_key("CHANGE_ACCS_LNAME") or {}
            if event.sender_id not in CHANGE_ACCS_LNAME:                 
                CHANGE_ACCS_LNAME.update({event.sender_id: "yes"})
                DB.set_key("CHANGE_ACCS_LNAME", CHANGE_ACCS_LNAME)

            CHANGE_ACCS_BIO = DB.get_key("CHANGE_ACCS_BIO") or {}
            if event.sender_id not in CHANGE_ACCS_BIO:                 
                CHANGE_ACCS_BIO.update({event.sender_id: "yes"})
                DB.set_key("CHANGE_ACCS_BIO", CHANGE_ACCS_BIO)

            CHANGE_ACCS_USERNAME = DB.get_key("CHANGE_ACCS_USERNAME") or {}
            if event.sender_id not in CHANGE_ACCS_USERNAME:                 
                CHANGE_ACCS_USERNAME.update({event.sender_id: "yes"})
                DB.set_key("CHANGE_ACCS_USERNAME", CHANGE_ACCS_USERNAME)

            CHANGE_ACCS_PHOTO = DB.get_key("CHANGE_ACCS_PHOTO") or {}
            if event.sender_id not in CHANGE_ACCS_PHOTO:                 
                CHANGE_ACCS_PHOTO.update({event.sender_id: "yes"})
                DB.set_key("CHANGE_ACCS_PHOTO", CHANGE_ACCS_PHOTO)

            if not event.is_private or event.out:
                return

            if admin_only and event.sender_id != bot.admin.id:
                return

            try:
                await bot(functions.channels.GetParticipantRequest(
                    channel=CHANNEL,
                    participant=event.sender_id
                ))
            except:
                info = await bot.get_entity(event.sender_id)
                text = f"**👋 Hi {info.first_name}!**\n\n**🔶 For Use From Bot Pleae Join To My Channel To Receive Updates And More ...**\n\n __• Channel:__ **@{CHANNEL}**"
                buttons = [[Button.url("• Join Channel •", f"https://t.me/{CHANNEL}")], [Button.inline("Check Join ✅", data=f"checkjoin:{event.sender_id}")]]
                return await event.reply(text, buttons=buttons)

            if event.text == "🔙":
                return await event.reply("**• Ok, Backed To Home Page!**", buttons=main_menu)

            print(event.text)

            try:
                await func(event)
            except:
                await bot.send_message(LOG_GROUP, f"**#Error**\n\n**• New Error:** ( `{format_exc()}` )")
        bot.add_event_handler(wrapper, events.MessageEdited(pattern=pattern, **kwargs))
        bot.add_event_handler(wrapper, events.NewMessage(pattern=pattern, **kwargs))
        return wrapper
    return decorator
