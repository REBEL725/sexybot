# PLUGIN MADE BY @REBEL_IS_OP FOR REBELBOT
# KEEP CREDITS ELSE GAY

from REBELBOT.utils import admin_cmd

from userbot.cmdhelp import CmdHelp


@borg.on(admin_cmd(pattern="baby ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            """HEYY BABYπππ HOW ARE  YOU  π AP KO PATA HA MA BASS AP KK LIYA HUU ISS DUNIYA MA ORR AP MERI JAAN HOO ππππ₯°. ORR AP KKK BAAD KOI NAHI HAAA MERA π₯Ίπ₯Ίπ₯Ί. AP JAB NAHI HOO TII HO TABB KOI MERE SA BAAT  NAHI KARTA HAA π₯Ίπ₯Ί. BUT MERE KO ISS SA KOI FIRK NAHI PADTA HAππ. BASS AP MERA SATH HOO YAHI π₯°π₯°. BHUT JADA HAA πβ£οΈ I LOVE YOU MY SWEET HEART TUM MERI JAAN HO ORR MAA THUMARA. LIYA  KUCH VV KAR SAKTA HUUU"""
        )


CmdHelp("baby").add_command("baby", "<tag your gf>", "send your gf and enjoy.").add()
