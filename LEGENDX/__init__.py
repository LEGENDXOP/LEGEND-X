from LEGEND.events import register as LEGENDX22
from LEGEND import telethn as bot
from LEGEND import API_ID, API_HASH
from LEGEND.events import *
from telethon import TelegramClient
if STRING_SESSION:
    user = TelegramClient(StringSession(STRING_SESSION), API_ID, API_HASH)
else:
     print ("please add StringSession var")

try:
     ubot.start()
except Exception as e:
     print(e)
        
# COPYRIGHT (C) BY LEGENDX22 AND PROBOYX
