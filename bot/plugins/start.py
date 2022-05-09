from pyrogram import filters
from bot import bot

@bot.on_message(filters.command(["start"]))
async def start(client, message):
    await message.reply("**• Hello There!**")
