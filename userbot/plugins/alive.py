# Thanks to @D3_krish
# Porting in REBELUSERBOT by REBEL75

import asyncio

from telethon import version

from userbot import ALIVE_NAME, REBELversion
from userbot.cmdhelp import CmdHelp
from userbot.utils import admin_cmd, sudo_cmd

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "REBELBOT"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

REBEL = bot.uid

edit_time = 4
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/76dd5605de7340568a904.mp4"
file2 = "https://telegra.ph/file/b765c0daec4a63c286e34.mp4"
file3 = "https://telegra.ph/file/956883ad3a92d3f816040.mp4"
file4 = "https://telegra.ph/file/b765c0daec4a63c286e34.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥𝐑𝐄𝐁𝐄𝐋 𝐁𝐎𝐓  𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                🔰ᗰᗩՏTᗴᖇ🔰\n      **『😈[{DEFAULTUSER}](tg://user?id={REBEL})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `𝚅𝚎𝚛𝚜𝚒𝚘𝚗:` `{REBELversion}`\n"
pm_caption += f"┣•➳➠ `𝚂𝚞𝚍𝚘:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `𝙲𝚑𝚊𝚗𝚗𝚎𝚕:` [𝙹𝙾𝙸𝙽](https://t.me/REBELBOT_SUPPORT)\n"
pm_caption += f"┣•➳➠ `𝙲𝚛𝚎𝚊𝚝𝚘𝚛:` [𝚁𝙴𝙱𝙴𝙻](https://t.me/REBEL_IS_OP)\n"
pm_caption += f"┣•➳➠ `𝚂𝚞𝚙𝚙𝚘𝚛𝚝𝚎𝚛:` [𝙽𝙸𝚂𝙷𝚄](https://t.me/nishuop)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥𝐑𝐄𝐏𝐎🔥](https://github.com/REBEL75/REBELBOTOP) 🔹 [📜𝐋𝐢𝐜𝐞𝐧𝐬𝐞📜](https://github.com/REBEL75/REBELBOTOP/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1, caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command("alive", None, "To check am i alive").add_command(
    "rebel", None, "To check am i alive with your favorite alive pic"
).add()
