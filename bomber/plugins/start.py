from bomber.events import Cmd

@Cmd(pattern="start")
async def start(event):
    await event.reply("**• Hello There!**")
