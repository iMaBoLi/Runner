from manager import bot
from manager.events import Cmd
from manager.database import DB
from manager.steps import sstep

@Cmd(pattern="(?i)^\/start$")
async def start(event):
    USERS = DB.get_key("BOT_USERS") or []
    info = await event.client.get_entity(event.sender_id)
    sstep(info.id, "free")
    if info.id not in USERS:
        USERS.append(info.id)
        DB.set_key("BOT_USERS", USERS)
    await event.reply(f"**👋 Hi {info.mention}!**\n**😘 Welcome To My Acc Manager Robot!**\n\n**💡 Maker: @{bot.admin.username}**")

@Cmd(pattern="(?i)^\/cancel$")
async def start(event):
    sstep(event.sender_id, "free")
    await event.reply("**• Successfuly Canceled!**")
