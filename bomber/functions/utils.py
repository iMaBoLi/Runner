from pathlib import Path
import os
import sys
import time
import logging
import math
import importlib
import glob
import shlex
import asyncio
import functools
import re
import random

def shuffle(list, count=5):
    for i in range(count):
        r = random.random()
        random.shuffle(list, lambda: r)
    return list

async def runcmd(cmd):
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(*args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return stdout.decode("utf-8", "replace").strip(), stderr.decode("utf-8", "replace").strip()

def chunks(elements, size):
    n = max(1, size)
    return (elements[i:i + n] for i in range(0, len(elements), n))

def load_plugins(folder):
    files = glob.glob(f"userbot/{folder}/*.py")
    for name in files:
        plugin_name = os.path.basename(name)
        try:
            path = Path(f"userbot/{folder}/{plugin_name}")
            name = "userbot.{}.{}".format(folder , plugin_name.replace(".py" , ""))
            spec = importlib.util.spec_from_file_location(name, path)
            load = importlib.util.module_from_spec(spec)
            load.logger = logging.getLogger(plugin_name)
            spec.loader.exec_module(load)
            sys.modules[name] = load
            print(f"""• Bot Has Imported ( {plugin_name.replace(".py", "")} ) Plugin""")
        except Exception as e:
            print(f"""• Bot Can't Import ( {plugin_name.replace(".py", "")} ) Plugin - Error : < {e} >""")

def convert_bytes(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s%s" % (s, size_name[i])

def convert_time(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    months, days = divmod(days, 30)
    result = (
        ((str(months) + "m:") if months else "")
        + ((str(weeks) + "w:") if weeks else "")
        + ((str(days) + "d:") if days else "")
        + ((str(hours) + "h:") if hours else "")
        + ((str(minutes) + "m:") if minutes else "")
        + ((str(seconds) + "s") if seconds else "")
    )
    if result.endswith(":"):
        return result[:-1]
    return result
