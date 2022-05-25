from . import bot
from telethon import events
from traceback import format_exc
import os
import sys
import re

def Cmd(
    pattern=None,
    admin_only=False,
    **kwargs,
):
    def decorator(func):
        async def wrapper(event):
            if not event.is_private:
                return
            if event.out:
                return
            if event.fwd_from and event.via_bot_id:
                return
            if admin_only and event.sender_id != bot.admin.id:
                return
            try:
                await func(event)
            except:
                return
        bot.add_event_handler(wrapper, events.MessageEdited(pattern=pattern, **kwargs))
        bot.add_event_handler(wrapper, events.NewMessage(pattern=pattern, **kwargs))
        return wrapper
    return decorator
