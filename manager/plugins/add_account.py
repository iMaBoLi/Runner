from manager import bot
from manager.events import Cmd
from telethon import TelegramClient
from manager.database import DB
from manager.steps import steps, sstep, gstep
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

@Cmd(pattern="(?i)^\/add$")
async def add(event):
    await event.reply("**•Ok, Send Your Phone Number:**\n\n__• Ex: +19307777777 __")
    sstep(event.sender_id, "send_number")

@Cmd()
async def add_account(event):
    if gstep(event.sender_id) == "send_number" and re.search("[\+]?[1-9][0-9 .\-\(\)]{8,16}[0-9]", event.text):
        edit = await event.reply("`• Please Wait . . .`")
        phone = event.text
        client = TelegramClient(f"sessions/{phone}.session", 13367220, "52cdad8b941c04c0c85d28ed6b765825")
        await client.connect()
        try:
            scode = await client.send_code_request(phone)
            sstep(event.sender_id, f"send_code:{phone}")
            await edit.edit(f"**• Ok, Send Your Telegram Code For:** ( `{phone}` )")
        except PhoneNumberInvalidError:
            sstep(event.sender_id, "free")
            os.remove(f"sessions/{message.text}.session")
            return await edit.edit("**• Your Phone Number Is Invalid!**")
        except PhoneNumberFloodError:
            sstep(event.sender_id, "free")
            os.remove(f"sessions/{message.text}.session")
            return await edit.edit("**• Your Phone Number Is Flooded!**")
        except PhoneNumberBannedError:
            sstep(event.sender_id, "free")
            os.remove(f"sessions/{message.text}.session")
            return await edit.edit("**• Your Phone Number Is Banned!**")
    elif "send_code" in gstep(event.sender_id):
        edit = await event.reply("`• Please Wait . . .`")
        phone = gstep(event.sender_id).split(":")[1]
        client = TelegramClient(f"sessions/{phone}.session", 13367220, "52cdad8b941c04c0c85d28ed6b765825")
        await client.connect()
        phone_code = event.text
        try:
            await client.sign_in(phone, phone_code)
        except PhoneCodeInvalidError:
            return await edit.edit("**• Your Code Is Invalid!**\n\n__• Check Code Again!__")
        except PhoneCodeExpiredError:
            sstep(event.sender_id, "free")
            return await edit.edit("**• Your Code Is Expired!**")
        except SessionPasswordNeeded:
            return
