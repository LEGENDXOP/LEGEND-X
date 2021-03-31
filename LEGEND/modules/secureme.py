# COPYRIGHT (C) 2021 BY LEGENDX2222 AND ROSELOVERX
#CREDITS #TEAMLEGEND
from LEGEND_X import bot as tbot, LEGENDX2222
import os
import secureme
from base64 import b64decode, b64encode

@LEGENDX2222(pattern="^/encrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          lel = await event.get_reply_message()
          cmd = lel.text
    else:
          cmd = event.pattern_match.group(1)
    Text = cmd
    k = secureme.encrypt(Text)
    await event.reply(k)

@LEGENDX2222(pattern="^/decrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          lel = await event.get_reply_message()
          ok = lel.text
    else:
          ok = event.pattern_match.group(1)
    Text = ok
    k = secureme.decrypt(Text)
    await event.reply(k)
@LEGENDX2222(pattern="/base (.*)")
async def crypt (event):
  try:
    LEGENDX22 = event.pattern_match.group(1)
    ok = b64encode(f"{LEGENDX22}".encode())
    await event.reply(ok)
  except Exception as e:
    await event.reply(f'can you give me some text ?\n\n\n {e}')

@LEGENDX2222(pattern="/-base (.*)")
async def haha(event):
  try:
    LEGENDX22 = event.pattern_match.group(1)
    ok = b64decode(f"{LEGENDX22}".decode())
    await event.reply(ok)
  except Exception as e:
    await event.reply(f'can you give me some text ?\n\n\n{e}')

__mod_name__="Secure♟️"
__help__="""
- /encrypt <text> for crypting
- /decrypt <text> for decoding
- /base <text> for crypting on base64
- /-base <text> for deciding on base64
"""
