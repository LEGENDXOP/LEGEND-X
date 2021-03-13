from LEGENDX import bot as tbot, LEGENDX22
import os
import secureme
from base64 import b64decode, b64encode

@LEGENDX22(pattern="^/encrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          lel = await event.get_reply_message()
          cmd = lel.text
    else:
          cmd = event.pattern_match.group(1)
    Text = cmd
    k = secureme.encrypt(Text)
    await event.reply(k)

@LEGENDX22(pattern="^/decrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          lel = await event.get_reply_message()
          ok = lel.text
    else:
          ok = event.pattern_match.group(1)
    Text = ok
    k = secureme.decrypt(Text)
    await event.reply(k)
@LEGENDX22(pattern="/base")
async def crypt (event):
  LEGENDX = event.pattern_match.group(1)
  if not LEGENDX == "":
    ok = b64dencode(f"{LEGENDX}".encode())
    await event.reply(ok)
  else:
    await event.reply('can you give me some text ?")

@LEGENDX22(pattern="/-base")
async def haha(event):
  LEGENDX = event.pattern_match.group(1)
  if not LEGENDX == "":
    ok = b64decode(f"{LEGENDX}".decode())
    await event.reply(ok)
  else:
    await event.reply('can you give me some text ?")

__mod_name__="secure"
__help__="""
- /encrypt <text> for crypting
- /decrypt <text> for decoding
- /base <text> for crypting on base64
- /-base <text> for deciding on base64
"""
