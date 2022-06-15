from manager import bot, LOG_GROUP
from telethon import TelegramClient, events, functions
from telethon.sessions import StringSession
from manager.database import DB
import re

@bot.on(events.CallbackQuery(data=re.compile("logout\:(.*)")))
async def logout(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    session = DB.get_key("USER_ACCS")[event.sender_id][phone]
    client = TelegramClient(StringSession(session), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
    await client.log_out()
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
    await bot.send_message(event.chat_id, codes)
    await event.answer("• Telegram Codes Sneded For You!", alert=True)

@bot.on(events.CallbackQuery(data=re.compile("resetauthorization\:(.*)")))
async def resetauthorization(event):
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
