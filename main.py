from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon import events, functions, types, Button
from datetime import datetime
from pathlib import Path
import traceback
import requests
import asyncio
import os
import sys
import io
import glob
import re
import json
import time

API_ID = 909317
API_HASH = "bae2fc6f671b02f9bea0473ed369a95f"
SESSION = "1BJWap1sBu701IEUb87VzdxbFUTKU-05U7NKYAksocxek4x05B-rqjJoUbqeaYnNDmnyWn8LsgtqDsaQXRdg52S4U3SxsWUbbj7rCAyGC5hQoLP5uLIuc227bLPvsc6ZWEUTy6Ee6cb0OrOdZ7w6ppeaEHYTtUbKJVJNnbAhXA2sL1W3tDmS6WJN9tpLhzJv4WqVW_aDvSlolZK3IEUOID3r35ST6I_wUu8I5SaeEbJ5MAvUcg3lCUZDMgQcvt8Ms7ytLo6dWJk3hcNyUUDOHuIaxGdz50B1bEGdG1OKcpPNYoc92RAaZMa8WiBSvQFmvAvlVI5mrCoSqcXLcaXVfl0avupg0kqw="

try:
    client = TelegramClient(
        session=StringSession(SESSION),
        api_id=API_ID,
        api_hash=API_HASH,
    ).start()
except Exception as error:
    print("• Login To Account Was Unsuccessful!")

async def runner(code , event):
    chat = await event.get_chat()
    reply = await event.get_reply_message()
    local = lambda out: print(_format.yaml_format(out))
    exec("async def coderunner(event , local, chat, chat_id, reply): "+ "".join(f"\n {line}" for line in code.split("\n")))
    return await locals()["coderunner"](event , local, chat, chat.id, reply)

@client.on(events.NewMessage(pattern="Run(?:\s|$)([\s\S]*)"))
async def runcodes(event):
    reply = await event.reply(f"**Running ...**")
    if event.text[4:]:
        cmd = "".join(event.text.split(maxsplit=1)[1:])
    else:
        return await reply.edit(f"**What Should I Run ?**")
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exec = None, None, None
    try:
        await runner(cmd , event)
    except:
        exec = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    result = "Success!"
    if exec:
        result = exec
    elif stderr:
        result = stderr
    elif stdout:
        result = stdout
    if len(result) < 4096:
        await reply.edit(f"**Results:**\n\n`{result}`")
    else:
        file = client.PATH + "OutPut.txt"
        open(file, "w").write(str(result))
        await client.send_file(event.chat_id, file , caption="**Code OutPut!**", reply_to=event.id)
        os.remove(file)
        await reply.delete()

client.run_until_disconnected()
