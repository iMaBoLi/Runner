from manager import bot, LOG_GROUP
from manager.events import Cmd
from telethon import events, Button
from . import main_menu, back_menu, panel_menu
from manager.database import DB

@Cmd(pattern="/panel", admin_only=True)
async def panel(event):
    await event.reply(f"", buttons=panel_menu)
