from manager import bot
from manager.events import Cmd
from telethon import TelegramClient
from telethon.sessions import StringSession
from . import main_menu, back_menu

@Cmd(pattern="Account Panel 🛠️")
async def acc_panel(event):
    async with bot.conversation(event.chat_id) as conv:
        send = await event.reply("**•Ok, Send Your Phone Number To Get Panel For This:**\n\n__• Ex: +19307777777 __", buttons=back_menu)
        response = await conv.get_response(send.id)
        phone = response.text 
    if phone == "🔙":
        return
    edit = await event.reply("`• Please Wait . . .`")
    client = TelegramClient(StringSession(), 13367220, "52cdad8b941c04c0c85d28ed6b765825")
    await client.connect()
