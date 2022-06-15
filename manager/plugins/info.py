from manager import bot, LOG_GROUP
from telethon import events, Button
from manager.events import Cmd
from manager.database import DB
import re

@Cmd(pattern="My Info 📝")
async def info(event):
    info = await bot.get_entity(event.sender_id)
    acc_count = DB.get_key("USER_ACCS_COUNT")[event.sender_id]
    text = f"""
**• Your Information:**

**• Name:** ( `{info.first_name}` )
**• UserID:** ( `{info.id}` )

**• Accounts Count:** ( `{acc_count}` )
"""
    await event.reply(text, buttons=[[Button.inline("• Account List •", data=f"accs:{event.sender_id}")]])

@bot.on(events.CallbackQuery(data=re.compile("accs\:(.*)")))
async def acc_list(event):
    id = int(event.pattern_match.group(1).decode('utf-8'))
    accs = DB.get_key("USER_ACCS")[event.sender_id]
    if len(accs) == 0:
        return await event.answer("• Not Account Added To Bot!", alert=True)
    text = "• Your Accounts List:\n\n"
    count = 1
    for acc in accs:
        text += "{count} - {acc}"
        count += 1
    open(f"{event.sender_id}.txt", "w").write(str(text))
    await event.reply("**• Your Account List!**", file=f"{event.sender_id}.txt")
