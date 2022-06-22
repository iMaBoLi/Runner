from manager import bot
from manager.events import Cmd
from telethon import TelegramClient, Button
from telethon.sessions import StringSession
from manager.database import DB
from . import main_menu, back_menu
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
async def add_account(event):
    async with bot.conversation(event.chat_id) as conv:
        send = await event.reply("**•Ok, Send Your Phone Number:**\n\n__• Ex: +19307777777 __", buttons=back_menu)
        response = await conv.get_response(send.id)
        phone = response.text
    if phone in DB.get_key("CMD_LIST"):
        return
    edit = await event.reply("`• Please Wait . . .`")
    client = TelegramClient(StringSession(), 13367220, "52cdad8b941c04c0c85d28ed6b765825", device_model="• Acc-Manager 🔐")
    await client.connect()
    try:
        scode = await client.send_code_request(phone)
        async with bot.conversation(event.chat_id) as conv:
            send = await edit.edit(f"**• Ok, Send Your Telegram Code For:** ( `{phone}` )")
            response = await conv.get_response(send.id, timeout=60)
            phone_code = response.text
        if phone_code in DB.get_key("CMD_LIST"):
            return
    except PhoneNumberInvalidError:
        return await edit.edit("**• Your Phone Number Is Invalid!**", buttons=main_menu(event))
    except PhoneNumberFloodError:
        return await edit.edit("**• Your Phone Number Is Flooded!**", buttons=main_menu(event))
    except PhoneNumberBannedError:
        return await edit.edit("**• Your Phone Number Is Banned!**", buttons=main_menu(event))
    except TimeoutError:
        return await edit.edit("**• Your Conversation Has Been Canceled, Try Again!**", buttons=main_menu(event))
    edit = await event.reply("`• Please Wait . . .`")
    phone_code = phone_code.replace(" ", "")
    try:
        await client.sign_in(phone=phone, code=phone_code, password=None)
        session = client.session.save()
        allaccs = DB.get_key("USER_ACCS")[event.sender_id]
        if phone not in allaccs:
            all = DB.get_key("USER_ACCS_COUNT")
            all[event.sender_id] += 1
            DB.set_key("USER_ACCS_COUNT", all)
        allaccs = DB.get_key("USER_ACCS")
        allaccs[event.sender_id][phone] = session
        DB.set_key("USER_ACCS", allaccs)
        buttons = [[Button.inline("• Yes •", data=f"yesedit:{phone}"), Button.inline("• No •", data=f"noedit:{phone}")]]
        await edit.edit(f"**• Successfuly Login To Your Account!**\n\n**• Your Session String:** ( `{session}` )\n\n**• Do You Want To Edit Your Account???**", buttons=buttons)
    except PhoneCodeInvalidError:
        return await edit.edit("**• Your Code Is Invalid, Try Again!**", buttons=main_menu(event))
    except PhoneCodeExpiredError:
        return await edit.edit("**• Your Code Is Expired, Try Again!**", buttons=main_menu(event))
    except SessionPasswordNeededError:
        async with bot.conversation(event.chat_id) as conv:
            send = await edit.edit(f"**• Ok, Send Your Account Password For:** ( `{phone}` )")
            response = await conv.get_response(send.id)
            password = response.text
        if password in DB.get_key("CMD_LIST"):
            return
        edit = await event.reply("`• Please Wait . . .`")
        try:
            await client.sign_in(password=password)
            session = client.session.save()
            allaccs = DB.get_key("USER_ACCS")[event.sender_id]
            if phone not in allaccs:
                all = DB.get_key("USER_ACCS_COUNT")
                all[event.sender_id] += 1
                DB.set_key("USER_ACCS_COUNT", all)
            allaccs = DB.get_key("USER_ACCS")
            allaccs[event.sender_id][phone] = session
            DB.set_key("USER_ACCS", allaccs)
            buttons = [[Button.inline("• Yes •", data=f"yesedit:{phone}"), Button.inline("• No •", data=f"noedit:{phone}")]]
            await edit.edit(f"**• Successfuly Login To Your Account!**\n\n**• Your Session String:** ( `{session}` )\n\n**• Do You Want To Edit Your Account???**", buttons=buttons)
        except PasswordHashInvalidError:
            return await edit.edit("**• Your Account Password Is Invalid, Try Again!**", buttons=main_menu(event))
