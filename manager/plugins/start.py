from manager import bot
from manager.events import Cmd
from . import main_menu
from manager.database.steps import sstep

@Cmd(pattern="(?i)^\/start$")
async def start(event):
    sstep(event.sender_id, "free")
    info = await bot.get_entity(event.sender_id)
    await event.reply(f"**👋 Hi {info.first_name}!**\n**😘 Welcome To Acc Manager Robot!**\n\n**💡 Maker: @{bot.admin.username}**", buttons=main_menu)

@Cmd(pattern="⬅️ Back")
async def start(event):
    sstep(event.sender_id, "free")
    await event.reply("**• Successfuly Backed To Home Page!**", buttons=main_menu)
