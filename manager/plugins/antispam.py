from manager import bot, LOG_GROUP
from manager.database import DB
from manager.events import Cmd
import time

async def is_spam(event):
    spams = DB.get_key("USER_SPAMS") or {}
    max, msgs = 5,10
    ban = DB.get_key("SPAM_BAN_TIME")
    user_id = event.sender_id
    try:
        usr = spams[user_id]
        usr["messages"] += 1
    except:
        spams[user_id] = {"next_time": int(time.time()) + max, "messages": 1, "banned": 0}
        usr = spams[user_id]
    if usr["banned"] >= int(time.time()):
        return True
    else:
        if usr["next_time"] >= int(time.time()):
            if usr["messages"] >= msgs:
                spams[user_id]["banned"] = time.time() + ban
                await event.reply(f"**🚫 You Are Spamed In Bot And Blocked For:** ( `{ban}s` ) 🚫")
                await bot.send_message(LOG_GROUP, f"**#New_Spam**\n\n**• UserID:** ( `{user_id}` )\n\n**• Ban Time:** ( `{ban}s` )")
                return True
        else:
            spams[user_id]["messages"] = 1
            spams[user_id]["next_time"] = int(time.time()) + max
    return False

@Cmd()
async def spam(event):
    if not event.sender_id == bot.admin.id and (await is_spam(event)):
        return
