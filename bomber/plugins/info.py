from bomber import bot
from bomber.events import Cmd
from bomber.database import DB

@Cmd(pattern="اطلاعات من 📝")
async def info(event):
    info = await bot.get_entity(event.sender_id)
    datainfo = DB.get_key("BOT_USERS")[info.id]
    await event.reply(f"""
**📋 اطلاعات شما:**

**🔶 آیدی عددی:** ( `{info.id}` )
**💡 تعداد امتیازات:** ( `{datainfo["coins"]}` )
**🧒 تعداد دعوت شده ها:** ( `{datainfo["invites"]}` )
**🎗 رتبه:** ( `{datainfo["rank"]}` )

**🆔 @MxBomber_Bot**
""")
