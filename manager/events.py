from . import bot, LOG_GROUP
from telethon import events
from manager.database import DB
from traceback import format_exc
import os
import sys
import re

def Cmd(
    pattern=None,
    admin_only=False,
    **kwargs,
):
    def decorator(func):
        async def wrapper(event):

            USERS = DB.get_key("BOT_USERS") or []
            if event.sender_id not in USERS:
                USERS.append(event.sender_id)
                DB.set_key("BOT_USERS", USERS)

            ACC_COUNT = DB.get_key("USER_ACC_COUNT") or {}
            if event.sender_id not in ACC_COUNT:                 
                ACC_COUNT.update({event.sender_id: 0})
                DB.set_key("USER_ACC_COUNT", ACC_COUNT)

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

            CHANGE_ACCS_PHOTO_COUNT = DB.get_key("CHANGE_ACCS_PHOTO_COUNT") or {}
            if event.sender_id not in CHANGE_ACCS_PHOTO_COUNT:                 
                CHANGE_ACCS_PHOTO_COUNT.update({event.sender_id: 3})
                DB.set_key("CHANGE_ACCS_PHOTO_COUNT", CHANGE_ACCS_PHOTO_COUNT)

            if not event.is_private or event.out:
                return
            if admin_only and event.sender_id != bot.admin.id:
                return
            try:
                await func(event)
            except:
                await bot.send_message(LOG_GROUP, f"**#Error**\n\n**• New Error:** ( `{format_exc()}` )")
        bot.add_event_handler(wrapper, events.MessageEdited(pattern=pattern, **kwargs))
        bot.add_event_handler(wrapper, events.NewMessage(pattern=pattern, **kwargs))
        return wrapper
    return decorator
