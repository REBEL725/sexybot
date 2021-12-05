import os
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from userbot import REBELversion, bot
from userbot.utils import load_module
from var import Var

os.system("pip install -U telethon")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("🔰ՏTᗩᖇT ᖇᗴᗷᗴᒪᗷOT🔰")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("⚡ᖇᗴᗷᗴᒪᗷOT ՏTᗩᖇTᑌᑭ ᑕOᗰᑭᒪᗴTᗴᗪ⚡")
    else:
        bot.start()


import glob

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


print(
    f"""Hello sir i am REBELBOT!! REBELBOT VERSION :- {REBELversion} YOUR REBELBOT IS READY! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @REBELBOT_SUPPORT ."""
)

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
