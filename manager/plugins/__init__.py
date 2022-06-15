from telethon import Button

main_menu = [
    [Button.text("Add Account 📥", resize=True, single_use=True)],
    [Button.text("Account Settings ⚙️", resize=True, single_use=True), Button.text("My Info 📝", resize=True, single_use=True)],
]

back_menu = [
    [Button.text("⬅️ Back", resize=True, single_use=True)],
]
