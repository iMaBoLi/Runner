from manager import bot
from manager.events import Cmd
from telethon import TelegramClient, Button
from telethon.sessions import StringSession
from manager.database import DB
from . import main_menu, back_menu
from manager.database.steps import steps, sstep, gstep
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

@Cmd(pattern="Add Account 📥")
async def add(event):
    sstep(event.sender_id, "add_account")
    await event.reply("**•Ok, Send Your Phone Number:**\n\n__• Ex: +19307777777 __", buttons=back_menu)

@Cmd()
async def add_account(event):
    if gstep(event.sender_id) == "add_account":
        edit = await event.reply("`• Please Wait . . .`")
        phone = event.text
        client = TelegramClient(StringSession(), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
        await client.connect()
        try:
            scode = await client.send_code_request(phone)
            async with client.conversation(event.chat_id) as conv:
                send = await edit.edit(f"**• Ok, Send Your Telegram Code For:** ( `{phone}` )")
                response = await conv.get_response(send.id)
                phone_code = response.text 
        except PhoneNumberInvalidError:
            return await edit.edit("**• Your Phone Number Is Invalid!**")
        except PhoneNumberFloodError:
            return await edit.edit("**• Your Phone Number Is Flooded!**")
        except PhoneNumberBannedError:
            return await edit.edit("**• Your Phone Number Is Banned!**")
        except TimeoutError:
            sstep(event.sender_id, "free")
            return await edit.edit("**• Your Conversation Has Been Canceled, Try Again!**", buttons=main_menu)
        edit = await event.reply("`• Please Wait . . .`")
        phone_code = event.text.replace(" ", "")
        try:
            await client.sign_in(phone, phone_code, phone_code_hash=phone_code_hash, password=None)
            buttons = [[Button.inline("• Yes •", data=f"yesedit:{phone}"), Button.inline("• No •", data=f"noedit:{phone}")]]
            session = client.session.save()
            allaccs = DB.get_key("USER_ACCS")[event.sender_id]
            if phone not in allaccs:
                all = DB.get_key("USER_ACCS_COUNT")
                all[event.sender_id] += 1
                DB.set_key("USER_ACCS_COUNT", all)
            allaccs = DB.get_key("USER_ACCS")
            allaccs[event.sender_id][phone] = session
            DB.set_key("USER_ACCS", allaccs)
            await edit.edit(f"**• Successfuly Login To Your Account!**\n\n**• Your Session String:** ( ||{session}|| )\n\n**• Do You Want To Edit Your Account???**", buttons=buttons)
            sstep(event.sender_id, "free")
        except PhoneCodeInvalidError:
            return await edit.edit("**• Your Code Is Invalid!**\n\n__• Check Code Again!__")
        except PhoneCodeExpiredError:
            sstep(event.sender_id, "free")
            return await edit.edit("**• Your Code Is Expired, Try Again!**", buttons=main_menu)
        except SessionPasswordNeededError:
            return await edit.edit(f"**• Ok, Send Your Account Password For:** ( `{phone}` )")
        edit = await event.reply("`• Please Wait . . .`")
        phone = gstep(event.sender_id).split(":")[1]
        client = TelegramClient(StringSession(), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
        await client.connect()
        password = event.text
        try:
            await client.sign_in(password=password)
            buttons = [[Button.inline("• Yes •", data=f"yesedit:{phone}"), Button.inline("• No •", data=f"noedit:{phone}")]]
            session = client.session.save()
            allaccs = DB.get_key("USER_ACCS")[event.sender_id]
            if phone not in allaccs:
                all = DB.get_key("USER_ACCS_COUNT")
                all[event.sender_id] += 1
                DB.set_key("USER_ACCS_COUNT", all)
            allaccs = DB.get_key("USER_ACCS")
            allaccs[event.sender_id][phone] = session
            DB.set_key("USER_ACCS", allaccs)
            await edit.edit(f"**• Successfuly Login To Your Account!**\n\n**• Your Session String:** ( ||{session}|| )\n\n**• Do You Want To Edit Your Account???**", buttons=buttons)
            sstep(event.sender_id, "free")
        except PasswordHashInvalidError:
            return await edit.edit("**• Your Account Password Is Invalid!**")
