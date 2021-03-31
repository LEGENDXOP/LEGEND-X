# COPYRIGHT (C) BY LEGENDX2222 AND PROBOYX 
"""
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
               MADE BY LEGENDX2222 AND PROBOYX
              COPYRIGHT BY LEGENDX22 AND PROBOY
                 CREDIT #TEAMLEGEND 
         IF YOU KANG THEN DONT REMOVE THIS LINES 
"""
from telethon import custom, events, Button
import os,re
from LEGEND import telethn as bot
from LEGEND import telethn as tgbot
from LEGEND.events import register 
@register(pattern="/myinfo")
async def proboyx(event):
  button = [[custom.Button.inline("CHECK",data="information")]]
  await bot.send_message(event.chat, "YOUR INFORMATION",buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    LEGENDX22 = "YOUR DETAILS BY GRAND OFFICIAL\n"
    LEGENDX22 += f"FIRST NAME : {PRO.first_name} \n"
    LEGENDX22 += f"LAST NAME : {PRO.last_name}\n"
    LEGENDX22 += f"YOU BOT : {PRO.bot} \n"
    LEGENDX22 += f"RESTRICTED : {PRO.restricted} \n"
    LEGENDX22 += f"USER ID : {boy}\n"
    LEGENDX22 += f"USERNAME : {PRO.username}\n"
    await event.answer(LEGENDX22, alert=True)
  except Exception as e:
    await event.reply(f"{e}")
