from manager import bot, LOG_GROUP
from manager.events import Cmd
from telethon import events, Button
from . import main_menu, back_menu, panel_menu
from manager.database import DB
import re

@Cmd(pattern="/panel", admin_only=True)
async def panel(event):
    await event.reply(f"**• Hi {bot.admin.first_name}!**\n\n**• Welcome To Admin Panel!**\n\n__• Use This Buttons!__", buttons=panel_menu())

@bot.on(events.CallbackQuery(data="onoff"))
async def change_status(event):
    status = "off" if DB.get_key("BOT_STATUS") == "on" else "on"
    DB.set_key("BOT_STATUS", status)
    await event.edit(buttons=panel_menu())
    status = "Actived ✅" if DB.get_key("BOT_STATUS") == "on" else "DeActived ❌"    
    await event.reply(f"**• Ok, The Bot Has Been Successfully {status}!**")
