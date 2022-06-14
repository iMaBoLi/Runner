from manager import bot, LOG_GROUP
from telethon import events, Button
import re

@bot.on(events.CallbackQuery(data=re.compile("yesedit\:(.*)")))
async def yesedit(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))

@bot.on(events.CallbackQuery(data=re.compile("noedit\:(.*)")))
async def yesedit(event):
    phone = str(event.pattern_match.group(1).decode('utf-8'))
    manage_menu = [
        [Button.inline("• Receive Codes •", data=f"getcodes:{phone}")],
    ]
    await event.edit(f"**• Accoutn Not Edited And Manage Menu Send For You:**\n\n__• Dont Delete This Menu!__")
    await event.reply(f"""
**#Manage_Menu**

**• Phone:** ( `{phone}` )

__• Dont Delete This Menu!__

**#Manage_Menu**
""", buttons=manage_menu)
