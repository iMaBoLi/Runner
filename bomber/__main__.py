from . import bot
from bot.functions.utils import load_plugins

async def setup():
    LOGS.info("• Starting Setup Plugins . . .")
    load_plugins("plugins")
    LOGS.info("• Setup Plugins Completed!")
    bot.me = await bot.get_me()
    LOGS.info("• Alien UserBot Has Been Start Now!")

bot.loop.run_until_complete(setup())
