from manager import bot, LOG_GROUP
from telethon import events, Button
from manager.events import Cmd
from manager.database import DB
import re

@Cmd(pattern="Accounts List 💡")
async def myaccs(event):
    accs = DB.get_key("USER_ACCS")[event.sender_id]
    if len(accs) == 0:
        return await event.answer("• Not Account Added To Bot!", alert=True)
    text = "• Your Accounts List:\n\n"
    count = 1
    for acc in accs:
        text += f"{count} - {acc}\n"
        count += 1
    open(f"{event.sender_id}.txt", "w").write(str(text))
    text = f"""
**• Your Accounts List:**

**• Count:** ( `{len(accs)}` )
"""
    await event.reply(text, file=f"{event.sender_id}.txt")
