from bomber import bot
from telethon import events
from bomber.database import DB

@bot.on(events.NewMessage(pattern="(?i)\/start"))
async def start(event):
    USERS = DB.get_key("BOT_USERS") or []
    info = await bot.get_entity(event.sender_id)
    if info.id not in USERS:
        USERS.append(info.id)
        DB.set_key("BOT_USERS", USERS)
        await event.reply(f"**• Hello {info.first_name}!**\n**• Welcome To SmsBomber Bot!**\n\n**• Creator: @MxAboli**")
    else:
        await event.reply(f"**• Hello Again {info.first_name}!**\n**• Welcome To SmsBomber Bot!**\n\n**• Creator: @MxAboli**\n\n\n__• Bot Updated . . .__")
