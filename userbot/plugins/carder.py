from faker import Faker
from REBELBOT import CmdHelp
from REBELBOT import bot as REBELBOT
from REBELBOT.utils import admin_cmd, edit_or_reply, sudo_cmd
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


@REBELBOT.on(admin_cmd("gencc$"))
@REBELBOT.on(sudo_cmd("gencc$", allow_sudo=True))
async def _(REBELevent):
    if REBELevent.fwd_from:
        return
    REBELcc = Faker()
    REBELname = REBELcc.name()
    REBELadre = REBELcc.address()
    REBELcard = REBELcc.credit_card_full()

    await edit_or_reply(
        REBELevent,
        f"__**👤 NAME :- **__\n`{REBELname}`\n\n__**🏡 ADDRESS :- **__\n`{REBELadre}`\n\n__**💸 CARD :- **__\n`{REBELcard}`",
    )


@REBELBOT.on(admin_cmd(pattern="bin ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="bin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    REBEL_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/bin {REBEL_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@REBELBOT.on(admin_cmd(pattern="vbv ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="vbv ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    REBEL_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/vbv {REBEL_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@REBELBOT.on(admin_cmd(pattern="key ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="key ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    REBEL_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/key {REBEL_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@REBELBOT.on(admin_cmd(pattern="iban ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="iban ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    REBEL_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/iban {REBEL_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@REBELBOT.on(admin_cmd(pattern="ccheck ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="ccheck ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    REBEL_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit("Checking...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/ss {REBEL_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


@REBELBOT.on(admin_cmd(pattern="ccbin ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="ccbin ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    REBEL_input = event.pattern_match.group(1)
    chat = "@carol5_bot"
    await event.edit(f"Trying to generate CC from the given bin `{REBEL_input}`")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, f"/gen {REBEL_input}")
            response = await response
        except YouBlockedUserError:
            await event.reply("Please Unblock @carol5_bot")
            return
        else:
            await event.delete()
            await event.client.send_message(event.chat_id, response.message)


CmdHelp("carder").add_command("gencc", None, "Generates fake cc...").add_command(
    "ccheck", "<query>", "Checks that the given cc is live or not"
).add_command(
    "iban", "<query>", "Checks that the given IBAN ID is live or not"
).add_command(
    "key", "<query>", "Checks the status of probided key"
).add_command(
    "vbv", "<query>", "Checks the vbv status of given card"
).add_command(
    "bin", "<query>", "Checks that the given bin is valid or not"
).add_command(
    "ccbin", "<bin>", "Generates CC from the given bin."
).add()
