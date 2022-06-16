from manager import bot
from manager.events import Cmd
from manager.database import DB
from time import gmtime, strftime

@Cmd(pattern="My Info 📝")
async def info(event):
    info = await bot.get_entity(event.sender_id)
    acc_count = len(DB.get_key("USER_ACCS")[event.sender_id])
    date = strftime("%Y/%m/%d - %H:%M:%S", gmtime())
    text = f"""
**• Your Information:**

**• Name:** ( `{info.first_name}` )

**• UserID:** ( `{info.id}` )


**• Accounts Count:** ( `{acc_count}` )

__{date}__
"""
    await event.reply(text)
