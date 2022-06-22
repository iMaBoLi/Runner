from manager import bot, LOG_GROUP
from manager.events import Cmd
from telethon import events, Button
from . import main_menu, back_menu, manage_menu
from manager.database import DB
import re

@Cmd(pattern="Support 🧒")
async def support(event):
    async with bot.conversation(event.chat_id) as conv:
        send = await event.reply("**•Ok, Please Send Your Message To Be Sent For Support:**", buttons=back_menu)
        response = await conv.get_response(send.id, timeout=60)
    if response.text in DB.get_key("CMD_LIST"):
        return
    buttons = [[Button.inline("• Response •", data=f"response:{event.sender_id}")]]
    send = await bot.send_message(LOG_GROUP, response)
    await send.reply(f"**#New_Message**\n\n**• UserID:** ( `{event.sender_id}` )", buttons=buttons)
    await response.reply(f"**• Ok, Your Message Successfuly Sended To Support!**\n\n__• Please Wait For Reponse!__", buttons=main_menu(event))

@bot.on(events.CallbackQuery(data=re.compile("response\:(.*)")))
async def ressupport(event):
    id = int(event.pattern_match.group(1).decode('utf-8'))
    async with bot.conversation(LOG_GROUP) as conv:
        send = await event.edit(f"**• Ok, Send Your Response Message For Send To:** ( `{id}` )")
        response = await conv.get_response(send.id)
    if response.text in DB.get_key("CMD_LIST"):
        return
    send = await bot.send_message(id, "**• Your Response From Support:**")
    await send.reply(response)
    await response.reply(f"**• Message Successfuly Sended To:** ( `{id}` )")
