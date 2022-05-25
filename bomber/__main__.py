from . import bot
from bomber.functions.utils import load_plugins

async def setup():
    LOGS.info("• Starting Setup Plugins . . .")
    load_plugins()
    LOGS.info("• Setup Plugins Completed!")
    bot.me = await bot.get_me()
    LOGS.info("• Bomber Has Been Start Now!")

bot.loop.run_until_complete(setup())
bot.run_until_disconnected()
