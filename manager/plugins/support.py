from manager import bot, LOG_GROUP
from manager.events import Cmd
from . import main_menu, back_menu, manage_menu
from manager.database import DB

@Cmd(pattern="Support 🧒")
async def support(event):
    async with bot.conversation(event.chat_id) as conv:
        send = await event.reply("**•Ok, Please Send Your Message To Be Sent For Bot Support:**", buttons=back_menu)
        response = await conv.get_response(send.id)
    if response.text == "🔙":
        return
    await response.reply(f"**• Ok, Your Message Successfuly Sended To Support!**\n\n__• Please Wait For Reponse!__", buttons=main_menu)
    async with bot.conversation(LOG_GROUP) as conv:
        if not response.media:
            send = await bot.send_message(LOG_GROUP, f"**#New_Message**\n\n**• UserID:** ( `{event.sender_id}` )\n**• Message:**\n\n`{response.text}`")
        else:
            await bot.send_message(LOG_GROUP, f"**#New_Message**\n\n**• UserID:** ( `{event.sender_id}` )\n**• Message:**")
            send = await response.forward_to(LOG_GROUP)
        response = await conv.get_response(send.id, timeout=1000)
    if response.text == "/cancel":
        return await response.reply("**• Ok, Response To This Message Has Been Canceled!**")
    if not response.media:
        await bot.send_message(event.sender_id, f"**• Your Response From Support:**\n\n`{response.text}`)
    else:
        await bot.send_message(event.sender_id, f"**• Your Response From Support:**")
        await bot.send_message(event.sender_id, response.text, file=response.media)
    await response.reply(f"**• Response Message Successfuly Sended To:** ( `{event.sender_id}` )")
