from manager import bot, LOG_GROUP
from telethon import events, Button
from manager.events import Cmd
from manager.database import DB
import re

@Cmd(pattern="My Accounts 💡")
async def myaccs(event):
    info = await bot.get_entity(event.sender_id)
    acc_count = len(DB.get_key("USER_ACCS")[event.sender_id]) 
    text = f"""
**• Your Accounts List:**

**• Count:** ( `{acc_count}` )
"""
    await event.reply(text, buttons=[[Button.inline("• Account List •", data=f"accs:{event.sender_id}")], [Button.inline("• Telethon Session List •", data=f"sessionstel:{event.sender_id}")]])

@bot.on(events.CallbackQuery(data=re.compile("accs\:(.*)")))
async def acc_list(event):
    id = int(event.pattern_match.group(1).decode('utf-8'))
    accs = DB.get_key("USER_ACCS")[event.sender_id]
    if len(accs) == 0:
        return await event.answer("• Not Account Added To Bot!", alert=True)
    text = "• Your Accounts List:\n\n"
    count = 1
    for acc in accs:
        text += f"{count} - {acc}\n"
        count += 1
    open(f"{event.sender_id}.txt", "w").write(str(text))
    await event.reply("**• Your Accounts List!**", file=f"{event.sender_id}.txt")

@bot.on(events.CallbackQuery(data=re.compile("sessionstel\:(.*)")))
async def session_list(event):
    id = int(event.pattern_match.group(1).decode('utf-8'))
    accs = DB.get_key("USER_ACCS")[event.sender_id]
    if len(accs) == 0:
        return await event.answer("• Not Account Added To Bot!", alert=True)
    text = "• Your Telethon Sessions List:\n\n"
    for acc in accs:
        text += f"{acc} - ( {accs[acc]} )\n"
    open(f"{event.sender_id}.txt", "w").write(str(text))
    await event.reply("**• Your Telethon Sessions List!**", file=f"{event.sender_id}.txt")
