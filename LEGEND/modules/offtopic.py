# MADE BY PROBOYX AND LEGENDX2222

from telethon import events
from LEGEND import telethn as client
@client.on(events.NewMessage(pattern='#offtopic|#ot'))
async def handler(event):
  if event.chat_id == -1001383980001 or event.chat_id == -1001365341799:
    try:
      ok = await event.get_reply_message()
      oo = event.chat.username
      pro = f"@{ok.sender.username} You are going offtopic\nyou got warn \nand also got banned \n\nofftopic [message](https://t.me/{event.chat.username}/{ok.id}) \nReporter : @{event.sender.username}\nif offtopic message is deleted\nofftopic message = {ok.message}"
      await client.send_message(event.chat_id, pro, link_preview=False)
    except:
      await event.reply("tag a message and type #ot or #offtopic")
  else:
     await event.reply("this chat not made for this command")
  
