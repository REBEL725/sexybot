from REBELBOT import CmdHelp
from REBELBOT.utils import admin_cmd
from REBELBOT.utils import edit_or_reply as eor
from REBELBOT.utils import sudo_cmd
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


@REBELBOT.on(admin_cmd(pattern="history ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="history ?(.*)", allow_sudo=True))
async def _(REBELevent):
    if REBELevent.fwd_from:
        return
    if not REBELevent.reply_to_msg_id:
        await eor(REBELevent, "`Please Reply To A User To Get This Module Work`")
        return
    reply_message = await REBELevent.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eor(REBELevent, "Need actual users. Not Bots")
        return
    await eor(REBELevent, "Checking...")
    async with REBELevent.client.conversation(chat) as conv:
        try:
            response1 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response2 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response3 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await conv.send_message("/search_id {}".format(victim))
            response1 = await response1
            response2 = await response2
            response3 = await response3
        except YouBlockedUserError:
            await REBELevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
            return
        if response1.text.startswith("No records found"):
            await eor(REBELevent, "User never changed his Username...")
        else:
            await REBELevent.delete()
            await REBELevent.client.send_message(REBELevent.chat_id, response2.message)


@REBELBOT.on(admin_cmd(pattern="unh ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="unh ?(.*)", allow_sudo=True))
async def _(REBELevent):
    if REBELevent.fwd_from:
        return
    if not REBELevent.reply_to_msg_id:
        await eor(REBELevent, "`Please Reply To A User To Get This Module Work`")
        return
    reply_message = await REBELevent.get_reply_message()
    chat = "Sangmatainfo_bot"
    victim = reply_message.sender.id
    if reply_message.sender.bot:
        await eor(REBELevent, "Need actual users. Not Bots")
        return
    await eor(REBELevent, "Checking...")
    async with REBELevent.client.conversation(chat) as conv:
        try:
            response1 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response2 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            response3 = conv.wait_event(
                events.NewMessage(incoming=True, from_users=461843263)
            )
            await conv.send_message("/search_id {}".format(victim))
            response1 = await response1
            response2 = await response2
            response3 = await response3
        except YouBlockedUserError:
            await REBELevent.reply("Please unblock ( @Sangmatainfo_bot ) ")
            return
        if response1.text.startswith("No records found"):
            await eor(REBELevent, "User never changed his Username...")
        else:
            await REBELevent.delete()
            await REBELevent.client.send_message(REBELevent.chat_id, response3.message)


CmdHelp("history").add_command(
    "history", "<reply to a user>", "Fetches the name history of replied user."
).add_command(
    "unh", "<reply to user>", "Fetches the Username History of replied users."
).add()
