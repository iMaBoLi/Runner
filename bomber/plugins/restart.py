from bomber import bot
from telethon import events
from bomber.functions.utils import runcmd

@bot.on(events.NewMessage(pattern="(?i)\/restart"))
async def start(event):
    await runcmd("bash start")
    await event.reply("**• Bomber Restarted!**")
