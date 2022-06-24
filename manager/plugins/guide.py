from manager import bot, LOG_GROUP
from manager.events import Cmd
from . import main_menu
from manager.database import DB

@Cmd(pattern="Guide 💡")
async def guide(event):
    guide_text = f"""
**• Welcome To Guide Of Bot:**

**❗ This Bot Help You To Save And Manage Your Telegram Account!**
**❗ This Bot Prevents Your Accounts From Being Deleted As Much As Possible!**

**• Possibilities:**

**🔶 Change Setting Of Your Account!**
**🔶 Get Telegram Codes From Your Account!**
**🔶 Get Sessions From Your Account And You Can Delete This Sessions!**
**🔶 Reset All Sessions From Your Account!**
     **And ...**

__• Thanks For Using!__
"""
    await event.reply(guide_text, buttons=main_menu(event))
