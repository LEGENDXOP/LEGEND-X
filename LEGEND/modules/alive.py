# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX

"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
                 MADE BY LEGENDX AND PROBOYX
                   CREDITS #TEAMLEGEND 
                PLEASE DON'T REMOVE CREDITS
"""

from telethon import events, Button, custom
import re, os
from LEGEND.events import register
from LEGEND import telethn as tbot
from LEGEND import telethn as tgbot
PHOTO = "https://telegra.ph/file/ae5a7b751569bb8b5062e.jpg"
@register(pattern=("/alive"))
async def awake(event):
  legendx = event.sender.first_name
  LEGENDX = "HELLO THIS IS Mewtwo bot \n\n"
  LEGENDX += "ALL SYSTEM WORKING PROPERLY\n\n"
  LEGENDX += "3.0 OS : 3.8 LATEST\n\n"
  LEGENDX += f"MY MASTER {legend} ☺️\n\n"
  LEGENDX += "FULLY UPDATED\n\n"
  LEGENDX += "TELETHON : 1.19.5 LATEST\n\n"
  LEGENDX += "THANKS FOR ADDING ME HERE"
  BUTTON = [[Button.url("DEVELOPER", "https://t.me/Swami_2_0_0_50"), Button.url("MASTER", "https://t.me/swami_2_0_0_5")]]
  BUTTON += [[custom.Button.inline("REPOSITORYS", data="LEGENDX")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=LEGENDX,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"LEGENDX")))
async def callback_query_handler(event):
# inline by Swami_2_0_0_5
  PROBOYX +=[[Button.url("SUPPORT CHANNEL", "https://t.me/mewtwobotsupport"), Button.url("SUPPORT GROUP", "https://t.me/mewtwo1_botsupport")]]
  PROBOYX +=[[Button.url("POKEMON GO FRIENDS", "https://t.me/letsplay_pokemongo"), Button.url("HELPER", "https://t.me/Swami_alt")]]
  PROBOYX +=[[custom.Button.inline("ALIVE", data="PROBOY")]]
  await event.edit(text=f"ALL DETAILS OF REPOS", buttons=PROBOYX)



@register(pattern=("/repo|/REPO"))
async def repo(event):
  await tbot.send_message(event.chat, "REPO OF MEWTWO 3.0", buttons=[[Button.url("⚜️REPO⚜️", "https://github.com/pogonoob/LEGEND-X")]])
# SWAMI_2_0_0_5

__help__ = """
 - /alive check bot alive or die
 - /repo for this bot repo
"""
__mod_name__ = "Alive⚜️"
