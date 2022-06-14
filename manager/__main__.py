from . import bot, ADMIN_ID

async def setup():
    print("• Starting Setup Plugins . . .")
    files = glob.glob(f"manager/plugins/*.py")
    for name in files:
        plugin_name = os.path.basename(name)
        try:
            path = Path(f"manager/plugins/{plugin_name}")
            name = "manager.plugins.{}".format(plugin_name.replace(".py" , ""))
            spec = importlib.util.spec_from_file_location(name, path)
            load = importlib.util.module_from_spec(spec)
            load.logger = logging.getLogger(plugin_name)
            spec.loader.exec_module(load)
            sys.modules[name] = load
            print(f"""• Bot Has Imported ( {plugin_name.replace(".py", "")} ) Plugin""")
        except Exception as e:
            print(f"""• Bot Can't Import ( {plugin_name.replace(".py", "")} ) Plugin - Error : < {e} >""")
    print("• Setup Plugins Completed!")
    bot.me = await bot.get_me()
    bot.admin = await bot.get_entity(ADMIN_ID)
    print("• Bot Has Been Start Now!")

bot.loop.run_until_complete(setup())
bot.run_until_disconnected()
