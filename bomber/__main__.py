from . import bot, ADMIN_ID
from bomber.functions.utils import load_plugins

async def setup():
    print("• Starting Setup Plugins . . .")
    load_plugins()
    print("• Setup Plugins Completed!")
    bot.me = await bot.get_me()
    bot.admin = await bot.get_entity(ADMIN_ID)
    print("• Bomber Has Been Start Now!")

bot.loop.run_until_complete(setup())
bot.run_until_disconnected()
