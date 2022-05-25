from bomber.events import Cmd
from bomber.database import DB

@Cmd(pattern="(?i)^\/start$")
async def start(event):
    USERS = DB.get_key("BOT_USERS") or {}
    info = await event.client.get_entity(event.sender_id)
    if info.id not in USERS:
        USERS.update({info.id: {"coins": 10, "invites": 0, "rank": "Bronze"}})
        DB.set_key("BOT_USERS", USERS)
        await event.reply(f"**• Hello {info.first_name}!**\n**• Welcome To SmsBomber Bot!**\n\n**• Creator: @MxAboli**")
    else:
        await event.reply(f"**• Hello Again {info.first_name}!**\n**• Welcome To SmsBomber Bot!**\n\n**• Creator: @MxAboli**\n\n\n__• Bot Updated . . .__")
