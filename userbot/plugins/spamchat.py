from REBELBOT.Config import Config
from REBELBOT.utils import admin_cmd, sudo_cmd

from userbot.cmdhelp import CmdHelp

LOGGER = Config.PLUGIN_CHANNEL
SUDO_WALA = Config.SUDO_USERS


@borg.on(admin_cmd(pattern="spmsg (.*)"))
@bot.on(sudo_cmd(pattern="spmsg (.*)", allow_sudo=True))
async def _(event):
    name = event.pattern_match.group(1)
    if event.fwd_from:
        return
    await event.edit(
        f"{name} {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name}{name}\n{name} {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name}\n {name} {name} {name} {name} {name} {name} {name}\n{name} {name}{name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name}{name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name}{name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name}{name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name}{name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}\n{name} {name} {name} {name} {name} {name} {name}"
    )


CmdHelp("spamchat").add_command("spmsg", "<name>", "name type long").add()
