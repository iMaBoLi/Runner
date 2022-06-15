from manager import bot
from manager.events import Cmd
from telethon import TelegramClient, Button
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
    sstep(event.sender_id, "send_number")
    await event.reply("**•Ok, Send Your Phone Number:**\n\n__• Ex: +19307777777 __", buttons=back_menu)

@Cmd()
async def add_account(event):
    if gstep(event.sender_id) == "send_number" and re.search("[\+]?[1-9][0-9 .\-\(\)]{8,16}[0-9]", event.text):
        edit = await event.reply("`• Please Wait . . .`")
        phone = event.text
        client = TelegramClient(f"sessions/{phone}.session", 13367220, "52cdad8b941c04c0c85d28ed6b765825")
        await client.connect()
        try:
            scode = await client.send_code_request(phone)
            sstep(event.sender_id, f"send_code:{phone}:{scode.phone_code_hash}")
            return await edit.edit(f"**• Ok, Send Your Telegram Code For:** ( `{phone}` )")
        except PhoneNumberInvalidError:
            os.remove(f"sessions/{message.text}.session")
            return await edit.edit("**• Your Phone Number Is Invalid!**")
        except PhoneNumberFloodError:
            os.remove(f"sessions/{message.text}.session")
            return await edit.edit("**• Your Phone Number Is Flooded!**")
        except PhoneNumberBannedError:
            os.remove(f"sessions/{message.text}.session")
            return await edit.edit("**• Your Phone Number Is Banned!**")
    elif "send_code" in gstep(event.sender_id):
        edit = await event.reply("`• Please Wait . . .`")
        phone = gstep(event.sender_id).split(":")[1]
        phone_code_hash = gstep(event.sender_id).split(":")[2]
        client = TelegramClient(f"sessions/{phone}.session", 13367220, "52cdad8b941c04c0c85d28ed6b765825")
        await client.connect()
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
            allaccs[phone] = session
            DB.set_key("USER_ACCS", allaccs)
            await edit.edit("**• Successfuly Login To Your Account!**\n\n**• Do You Want To Edit Your Account???**", buttons=buttons)
            sstep(event.sender_id, "free")
            os.remove(f"sessions/{message.text}.session")
        except PhoneCodeInvalidError:
            return await edit.edit("**• Your Code Is Invalid!**\n\n__• Check Code Again!__")
        except PhoneCodeExpiredError:
            sstep(event.sender_id, "free")
            return await edit.edit("**• Your Code Is Expired!**")
        except SessionPasswordNeededError:
            sstep(event.sender_id, f"send_password:{phone}")
            return await edit.edit(f"**• Ok, Send Your Account Password For:** ( `{phone}` )")
    elif "send_password" in gstep(event.sender_id):
        edit = await event.reply("`• Please Wait . . .`")
        phone = gstep(event.sender_id).split(":")[1]
        client = TelegramClient(f"sessions/{phone}.session", 13367220, "52cdad8b941c04c0c85d28ed6b765825")
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
            add_acc(event.sender_id, phone, session)
            await edit.edit("**• Successfuly Login To Your Account!**\n\n**• Do You Want To Edit Your Account???**", buttons=buttons)
            sstep(event.sender_id, "free")
            os.remove(f"sessions/{phone}.session")
        except PasswordHashInvalidError:
            return await edit.edit("**• Your Account Password Is Invalid!**")
