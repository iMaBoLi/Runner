from manager import bot
from manager.events import Cmd
from manager.database import DB
from manager.steps import sstep
from . import main_menu

@Cmd(pattern="(?i)^\/start$")
async def start(event):
    USERS = DB.get_key("BOT_USERS") or []
    info = await event.client.get_entity(event.sender_id)
    sstep(info.id, "free")
    if info.id not in USERS:
        USERS.append(info.id)
        DB.set_key("BOT_USERS", USERS)
    await event.reply(f"**👋 Hi {info.mention}!**\n**😘 Welcome To My Acc Manager Robot!**\n\n**💡 Maker: @{bot.admin.username}**", buttons=main_menu)

@Cmd(pattern="⬅️ Back")
async def start(event):
    sstep(event.sender_id, "free")
    await event.reply("**• Successfuly Backed To Home Page!**", buttons=main_menu)
