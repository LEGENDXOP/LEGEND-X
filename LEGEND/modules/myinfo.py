# COPYRIGHT (C) BY LEGENDX22 AND PROBOYX 
"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
               MADE BY LEGENDX22 AND PROBOYX
              COPYRIGHT BY LEGENDX AND PROBOY
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
    LEGENDX = "YOUR DETAILS BY GRAND OFFICIAL\n"
    LEGENDX += f"FIRST NAME : {PRO.first_name} \n"
    LEGENDX += f"LAST NAME : {PRO.last_name}\n"
    LEGENDX += f"YOU BOT : {PRO.bot} \n"
    LEGENDX += f"RESTRICTED : {PRO.restricted} \n"
    LEGENDX += f"USER ID : {boy}\n"
    LEGENDX += f"USERNAME : {PRO.username}\n"
    await event.answer(LEGENDX, alert=True)
  except Exception as e:
    await event.reply(f"{e}")
