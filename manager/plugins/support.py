from manager import bot, LOG_GROUP
from manager.events import Cmd
from . import main_menu, back_menu, manage_menu
from manager.database import DB

@Cmd(pattern="Support 🧒")
async def acc_panel(event):
    async with bot.conversation(event.chat_id) as conv:
        send = await event.reply("**•Ok, Please Send Your Message To Be Sent For Bot Support:**", buttons=back_menu)
        response = await conv.get_response(send.id)
        mes = response.text
    if mes == "🔙":
        return
    async with bot.conversation(LOG_GROUP) as conv:
        send = await bot.send_message(LOG_GROUP, f"**#New_Message**\n\n**• UserID:** ( `{event.sender_id}` )\n**• Message:**\n`{mes}`")
        response = await conv.get_response(send.id, timeout=1000)
        pas = response.text
    if pas == "/cancel":
        return await response.reply("**• Ok, Response To This Message Has Been Canceled!**")
    await bot.send_message(event.sender_id, f"**• Your Response From Support:**\n\n`{pas}`")
    await response.edit(f"**• Message Successfuly Sended To:** ( `{event.sender_id}` )\n\n**• Message:** \n\n`{pas}`")
