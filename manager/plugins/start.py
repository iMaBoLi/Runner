from manager import bot
from manager.events import Cmd
from manager.database import DB

@Cmd(pattern="(?i)^\/start$", func=lambda e: e.is_private)
async def start(event):
    USERS = DB.get_key("BOT_USERS") or []
    info = await event.client.get_entity(event.sender_id)
    if info.id not in USERS:
        USERS.append(info.id)
        DB.set_key("BOT_USERS", USERS)
    await event.reply(f"**👋 Hi {info.mention}!**\n**😘 Welcome To My Acc Manager Robot!**\n\n**💡 Maker: @{bot.admin.username}**")
