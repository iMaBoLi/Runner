from manager import bot, LOG_GROUP
from manager.events import Cmd
from telethon import events, Button
from . import main_menu, back_menu, panel_menu
from manager.database import DB
import re
import asyncio

@Cmd(pattern="/panel", admin_only=True)
async def panel(event):
    await event.reply(f"**• Hi {bot.admin.first_name}!**\n\n**• Welcome To Admin Panel!**\n\n__• Use This Buttons!__", buttons=panel_menu())

@bot.on(events.CallbackQuery(data="onoff"))
async def change_status(event):
    status = "off" if DB.get_key("BOT_STATUS") == "on" else "on"
    DB.set_key("BOT_STATUS", status)
    if status == "on":
        DB.set_key("USER_OFF_STATUS", [])
    await event.edit(buttons=panel_menu())
    status = "Actived ✅" if DB.get_key("BOT_STATUS") == "on" else "DeActived ❌"    
    await event.reply(f"**• Ok, The Bot Has Been Successfully {status}!**")

@bot.on(events.CallbackQuery(data="sendtoall"))
async def sendtoall(event):
    async with bot.conversation(event.chat_id) as conv:
        send = await event.reply("**•Ok, Please Send Your Message To Be Sent For Bot Users:**", buttons=back_menu)
        response = await conv.get_response(send.id)
    if response.text == "🔙":
        return
    users = DB.get_key("BOT_USERS")
    count = 0
    for user in users:
        await bot.send_message(int(user), response)
        count += 1
        await asyncio.sleep(0.2)
    await response.reply(f"**• Ok, Your Message Successfuly Sended To** `{count}` **User From** `{len(users)}` **Users!**", buttons=main_menu)
