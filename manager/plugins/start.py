from manager import bot, CHANNEL
from telethon import events, functions
from . import main_menu, manage_menu
from manager.events import Cmd
from . import main_menu
import re

@Cmd(pattern="(?i)^\/start$")
async def start(event):
    info = await bot.get_entity(event.sender_id)
    await event.reply(f"**👋 Hi {info.first_name}!**\n**😘 Welcome To Acc Manager Robot!**\n\n**💡 Maker: @{bot.admin.username}**", buttons=main_menu)

@Cmd(pattern="🔙")
async def back(event):
    await event.reply("**• Ok, Backed To Home Page!**", buttons=main_menu)

@bot.on(events.CallbackQuery(data=re.compile("checkjoin\:(.*)")))
async def checkjoin(event):
    id = int(event.pattern_match.group(1).decode('utf-8'))
    try:
        await bot(functions.channels.GetParticipantRequest(
            channel=CHANNEL,
            participant=id
        ))
        info = await bot.get_entity(event.sender_id)
        await event.reply(f"**👋 Hi {info.first_name}!**\n**😘 Welcome To Acc Manager Robot!**\n\n**💡 Maker: @{bot.admin.username}**", buttons=main_menu)
        await event.delete()
    except:
        await event.answer("• You Are Not Joined To Channel!", alert=True)
