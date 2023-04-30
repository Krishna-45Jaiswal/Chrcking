# starting all clients
import logging
import platform

from LegendSB.start_bot import start_bot
from pyrogram import Client as call
from pyrogram import __version__ as py_version
from pyrogram import idle

from LegendGirl.Config import *

version = "v1.0"
group_username = "@LegendSpamBot"
logging.basicConfig(format="%(levelname)s  %(message)s", level=logging.INFO)


logging.getLogger("pyrogram").setLevel(logging.ERROR)
LOGS = logging.getLogger("BotSpam")

if STRING1:
    Client1 = call(
        "SpamBot1",
        api_id=APP_ID,
        api_hash=API_HASH,
        session_string=STRING1,
        plugins=dict(root="SpamBot/plugins"),
    )
    LOGS.info("Client 1 has been found")
else:
    LOGS.info("Client 1 not Found")


 async def Start_BotSpam():
    for i in range(1, 26):
        var = globals()[f"Client{i}"]
        if var is not None:
            await start_bot(var)
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    print(f"🔰 Spam Bot 🔰[INFO] : Group Username {group_username}")
    print(f"🔰 Spam Bot 🔰[INFO] : Version - {platform.python_version()}")
    print(f"🔰 Spam Bot 🔰[INFO]: SpamBot Version - {version}")
    print(f"🔰 Spam Bot 🔰[INFO]: Pyrogram Version - {py_version}")
    print("➖➖➖➖➖➖➖➖➖➖➖➖")
    await idle()
