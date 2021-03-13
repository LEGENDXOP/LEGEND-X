from LEGEND.events import register as LEGENDX22
from LEGEND import telethn as bot
from LEGEND import *
from LEGEND.events import *
try:
  from telethon import TelegramClient
  api_id = 1869668
  api_hash = '1037f965ea0a2db1136b9e83e5fc8d83'
  bot_token = '1561576171:AAGsHnIOZ_otsazWrrG07kEuD2ZLtgYySMU'
  ok = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
  ok.start()
  ok.run_until_disconnect()
except Exception as e:
  await bot.send_message(event.chat, e)
# COPYRIGHT (C) BY LEGENDX22 AND PROBOYX
