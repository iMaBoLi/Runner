from manager import bot, LOG_GROUP
from telethon import TelegramClient, events, functions
from telethon.sessions import StringSession
from manager.database import DB
from manager.functions import sql_session
import re

@bot.on(events.CallbackQuery(data=re.compile("logout\:(.*)")))
async def logout(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    session = DB.get_key("USER_ACCS")[event.sender_id][phone]
    client = TelegramClient(StringSession(session), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
    await client.log_out()
    allaccs = DB.get_key("USER_ACCS")[event.sender_id]
    if phone in allaccs:
        all = DB.get_key("USER_ACCS_COUNT")
        all[event.sender_id] -= 1
        DB.set_key("USER_ACCS_COUNT", all)
    allaccs = DB.get_key("USER_ACCS")
    del allaccs[event.sender_id][phone]
    DB.set_key("USER_ACCS", allaccs)
    await event.edit(f"**• Im LogOut From Your Account!**\n\n**• Account Number:** ( `{phone}` )")

@bot.on(events.CallbackQuery(data=re.compile("getcodes\:(.*)")))
async def getcodes(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    session = DB.get_key("USER_ACCS")[event.sender_id][phone]
    client = TelegramClient(StringSession(session), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
    count = 1
    codes = f"**• Telegram Codes For Number:** ( `{phone}` )\n\n"
    async for mes in client.iter_messages(777000):
        if match:= re.search("(\d*)\.", mes.text):
            if match.group(1):
                codes += f"**• {count} -**  `{match.group(1)}`\n"
                count += 1
    await bot.send_message(event.chat_id, codes)

@bot.on(events.CallbackQuery(data=re.compile("resauths\:(.*)")))
async def getauths(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    session = DB.get_key("USER_ACCS")[event.sender_id][phone]
    client = TelegramClient(StringSession(session), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
    accs = await client(functions.account.GetAuthorizationsRequest())
    all = len(accs.authorizations)
    cur = 0
    for acc in accs.authorizations:
        if not acc.current:
            await client(functions.account.ResetAuthorizationRequest(hash=acc.hash))
            cur += 1
    await event.answer(f"• Ok, {cur} Session From {all} Sessions Has Been Removed!", alert=True)

@bot.on(events.CallbackQuery(data=re.compile("getauths\:(.*)")))
async def getauths(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    session = DB.get_key("USER_ACCS")[event.sender_id][phone]
    client = TelegramClient(StringSession(session), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
    accs = await client(functions.account.GetAuthorizationsRequest())
    all = len(accs.authorizations)
    cur = 0
    for acc in accs.authorizations:
        if not acc.current:
            await client(functions.account.ResetAuthorizationRequest(hash=acc.hash))
            cur += 1
    await event.answer(f"• Ok, {cur} Session From {all} Sessions Has Been Removed!", alert=True)

@bot.on(events.CallbackQuery(data=re.compile("sesfile\:(.*)")))
async def getauths(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    session = DB.get_key("USER_ACCS")[event.sender_id][phone]
    file = await sql_session(session, phone)
    await event.reply(f"**• Session File For This Number:** ( `{phone}` )", file=file)

@bot.on(events.CallbackQuery(data=re.compile("sestel\:(.*)")))
async def getauths(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    session = DB.get_key("USER_ACCS")[event.sender_id][phone]
    await event.reply(f"**• Your Phone Is:** ( `{phone}` )\n\n**• Telethon String Session:** ( `{session}` )")
