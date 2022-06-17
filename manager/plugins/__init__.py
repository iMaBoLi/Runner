from manager import bot
from telethon import Button
from manager.database import DB

def main_menu(event):
    menu = [
        [Button.text("Add Account 📥", resize=True)],
        [Button.text("Account Settings ⚙️", resize=True), Button.text("Accounts List 📋", resize=True)],
        [Button.text("Account Panel 🛠️", resize=True), Button.text("My Info 📝", resize=True)],
        [Button.text("Guide 💡", resize=True), Button.text("Support 🧒", resize=True)],
    ]
    if event.sender_id == bot.admin.id:
        menu.append([Button.text("Admin Panel 🔐", resize=True)])
    return menu

back_menu = [
    [Button.text("🔙", resize=True)],
]

def manage_menu(phone):
    menu = [
        [Button.inline("• LogOut Bot •", data=f"logout:{phone}")],
        [Button.inline("• Reset Authorizations •", data=f"resauths:{phone}")],
        [Button.inline("• Get Authorizations •", data=f"getauths:{phone}"), Button.inline("• Get Telegram Codes •", data=f"getcodes:{phone}")],
        [Button.inline("• Get Session File •", data=f"sesfile:{phone}"), Button.inline("• Get Telethon Session •", data=f"sestel:{phone}")],
    ]
    return menu

def panel_menu():
    status = "✅" if DB.get_key("BOT_STATUS") == "on" else "❌"
    menu = [
        [Button.inline(f"{status} Bot Status {status}", data="onoff")],
        [Button.inline("• Send To All •", data="sendtoall")],
    ]
    return menu
