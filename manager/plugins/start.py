from manager import bot
from manager.events import Cmd
from . import main_menu

@Cmd(pattern="(?i)^\/start$")
async def start(event):
    info = await bot.get_entity(event.sender_id)
    await event.reply(f"**👋 Hi {info.first_name}!**\n**😘 Welcome To Acc Manager Robot!**\n\n**💡 Maker: @{bot.admin.username}**", buttons=main_menu)

@Cmd(pattern="🔙")
async def back(event):
    await event.reply("**• Ok, Backed To Home Page!**", buttons=main_menu)

            try:
                await bot(functions.channels.GetParticipantRequest(
                    channel=CHANNEL,
                    participant=event.sender_id
                ))
            except:
