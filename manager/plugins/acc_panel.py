from manager import bot
from manager.events import Cmd
from telethon import TelegramClient
from telethon.sessions import StringSession
from . import main_menu, back_menu, manage_menu
from manager.database import DB

@Cmd(pattern="Account Panel 🛠️")
async def acc_panel(event):
    async with bot.conversation(event.chat_id) as conv:
        send = await event.reply("**•Ok, Send Your Phone Number To Get Panel For This:**\n\n__• Ex: +19307777777 __", buttons=back_menu)
        response = await conv.get_response(send.id)
        phone = response.text 
    if phone == "🔙":
        return
    accs = DB.get_key("USER_ACCS")[event.sender_id]
    if phone not in accs:
        return await event.reply(f"**• You Are Not Added This Phone Number:** ( `{phone}` ) **To Bot!**")
    edit = await event.reply("`• Please Wait . . .`")
    menu = manage_menu(phone)
    await edit.edit(f"""
**#Manage_Menu**

**• Phone:** ( `{phone}` )

__• Dont Delete This Menu!__

**#Manage_Menu**
""", buttons=menu)
