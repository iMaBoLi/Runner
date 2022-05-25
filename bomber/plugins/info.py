from bomber import bot
from telethon import events
from bomber.database import DB

@Cmd(pattern="(?i)^\/myinfo$")
async def info(event):
    info = await bot.get_entity(event.sender_id)
    datainfo = DB.get_key("BOT_USERS")[info.id]
    await event.reply(f"""
**• Your Information:**

**• ID:** ( `{info.id}` )
**• Coins:** ( `{datainfo["coins"]}` )
**• Invites:** ( `{datainfo["invites"]}` )
**• Rank:** ( `{datainfo["rank"]}` )

**🆔 @MxBomber_Bot**
""")
