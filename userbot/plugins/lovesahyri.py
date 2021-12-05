# credit to kraken. madharchod plz dont copy
# Made By @veryhelful.
# thanks to kraken to give his plugin to edit and giving me idea
# all punjabi sahyri here are given by @Arwinder10


import asyncio
import random

from REBELBOT.utils import admin_cmd

from userbot import ALIVE_NAME
from userbot.cmdhelp import CmdHelp

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "@pyforub"

sawan = bot.uid


@bot.on(admin_cmd(pattern=r"plove$", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("@REBELBOT Making A Shayri.......")
    await asyncio.sleep(1.3)
    h = random.randrange(1, 9)
    if h == 1:
        await event.edit(
            f" Meri Kisi Gal Te Naraj Na Hovi,\nAkhian Nu Hanjua Nal Na Dhovi,\nMildi Ae Khushi Tenu Hasde Dekh Ke.\nSanu Maut Vi Aa Jave Ta Vi Na Rovi.\n\n\n✍️ {DEFAULTUSER}"
        )
    if h == 2:
        await event.edit(
            f"Dil Karda Ae Tere Kol Aa Ke Ruk Jaava,\nTeri Bukkal Wich Rakh Ke Sir Muk Jaava.\nHanju Ban Ke Digga Teriya Aakhaa Da,\nTere Bulla De Kol Aa Ke Sukk Jaava.\n\n\n✍️ {DEFAULTUSER}"
        )
    if h == 3:
        await event.edit(
            f"Tussi Hasde o sanu hasaan vaaste Tussi rone yo saanu rovaan vaaste Ek vaar rus ke ta vekho sohneyo Marr javange tuhanu manaan vaaste.\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 4:
        await event.edit(
            f"Jo pani wang paviter, pyar tan unu kehnde ne.\n\njo ikk di ho ke reh je, naar tan unu kehnde ne.\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 5:
        await event.edit(
            f"Khushboo teri yaari di saanu mehka jaandi hai,\n Teri har ik kitti hoyi gal saanu behka jaandi hai,\n Saah taan bahut der lagaande ne aun -jaan vich, \nHar saah ton pehle teri yaad aa jaandi hai.\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 6:
        await event.edit(
            f"Yaadan tereiya nu bhullna hun okha ho gaya...... \nJo detey ne tu Gum ohna nu sehna okha ho geya..... \nTu jaan lagey keh deta bhull ja mainu....... \nHun unna gallan nu bhullana okha ho gaya......\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 7:
        await event.edit(
            f"Ae chand chamkna chad vii de \nTeri chandni saanu staandi ae \nTera varga hai usda chehra \nTenu vekh ke usdi yaad aandi ae.\n\n\n✍️{DEFAULTUSER}  "
        )
    if h == 8:
        await event.edit(
            f"Tutte hoye Pemane ch jaam nahi aunda, \nIshq de mariz nu araam nahi aunda, \nO Dil todan walya tu e te sochya hunda,\n Tutya hoya Dil kisi de kamm nahi aunda.\n\n\n✍️{DEFAULTUSER}"
        )
    if h == 9:
        await event.edit(
            f"Meri kisi gal te naraj na hovi, \nAkhian nu hanjua nal na dhovi, \nMildi a khushi tenu hasde dekh ke\n Sanu maut v aa jave ta v na rovi…\n\n\n✍️{DEFAULTUSER}"
        )


CmdHelp("lovesahyri").add_command("plove", "<enjoy>", "love sahyri ").add()
