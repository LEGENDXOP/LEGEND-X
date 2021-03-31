# COPYRIGHT (C) 2021 BY LEGENDX2222 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
                 MADE BY LEGENDX22 AND PROBOYX
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGEND_X import xbot as tbot
from LEGEND_X import xbot as tgbot
PHOTO = "https://telegra.ph/file/b068fc8dc8d9be627bf85.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX22 = "HELLO THIS IS GRAND OFFICIAL \n\n"
  LEGENDX22 += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX22 += "GRAND OS : 3.8 LATEST\n\n"
  LEGENDX22 += f"MY MASTER {legendx} ☺️\n\n"
  LEGENDX22 += "FULLY UPDATED\n\n"
  LEGENDX22 += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX22 += "THANKS FOR ADD ME HERE"
  BUTTON = [[Button.url("MASTER", "https://t.me/LEGENDX2222"), Button.url("DEVLOPER", "https://t.me/proboyx")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="LEGENDX22")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX22,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX22")))
async def callback_query_handler(event):
# inline by LEGENDX2222 and PROBOYX🔥
  PROBOYX = [[Button.url("REPO-LEGEND", "https://github.com/LEGENDX22OP/LEGEND-BOT"), Button.url("REPO-ULTROID X", "https://github.com/ULTROID-OP/ULTROID-BOT")]]
  PROBOYX +=[[Button.url("DEPLOY-LEGEND", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Flegendxop%2Flegend-bot&template=https%3A%2F%2Fgithub.com%2FLEGENDX22OP%2FLEGEND-BOTP%2FLE"), Button.url("DEPLOY-ULTROID", "https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT&template=https%3A%2F%2Fgithub.com%2FULTROID-OP%2FULTROID-BOT")]]
  PROBOYX +=[[Button.url("TUTORIAL", "https://youtu.be/rGCSSFPsS4Q"), Button.url("STRING-SESSION", "https://repl.it/@legendx22/LEGEND-BOT#main.py")]]
  PROBOYX +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/LEGENDBOT_OFFICIAL"), Button.url("SUPPORT GROUP", "https://t.me/LEGEND_USERBOT_SUPPORT")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=PROBOYX)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"PROBOY")))
async def callback_query_handler(event):
  global PHOTO
  legendx = event.sender.first_name
# inline by LEGENDX2222 and PROBOYX 🔥
  LEGENDX22 = "HELLO THIS IS GRAND OFFICIAL \n\n"
  LEGENDX22 += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX22 += "GRAND OS : 3.8 LATEST\n\n"
  LEGENDX22 += f"MY MASTER {legendx} ☺️\n\n"
  LEGENDX22 += "FULLY UPDATED BOT\n\n"
  LEGENDX22 += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX22 += "THANKS FOR ADD ME HERE"
  BUTTONS = [[Button.url("MASTER", "https://t.me/LEGENDX2222"), Button.url("DEVLOPER", "https://t.me/proboyx")]]
  BUTTONS += [[custom.Button.inline("REPOSITORYS", data="LEGENDX22")]]
  await event.edit(text=LEGENDX22, buttons=BUTTONS)


@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF GRAND OFFICIAL", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/LEGENDX22OP/LEGEND-X")]])
# PROBOYX 🔥 LEGENDX2222

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
