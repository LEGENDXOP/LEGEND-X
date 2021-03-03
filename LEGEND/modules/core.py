from LEGEND import telethn as tbot, OWNER_ID, DEV_USERS
from LEGEND.events import register
import os
import asyncio
import os
import time
from datetime import datetime
from LEGEND import TEMP_DOWNLOAD_DIRECTORY as path
from LEGEND import TEMP_DOWNLOAD_DIRECTORY
from datetime import datetime

client = tbot

import time
from io import BytesIO
from pathlib import Path
from LEGEND import telethn as borg
from telethon import functions, types
from telethon.errors import PhotoInvalidDimensionsError
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import SendMediaRequest
@register(pattern="^/dox ?(.*)")
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.reply("reply to text message as `.ttf <file name>`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.reply("reply to text message as `.ttf <file name>`")

from LEGEND.events import load_module
import asyncio
import os
from datetime import datetime
from pathlib import Path

@register(pattern="^/install")
async def install(event):
    if event.fwd_from:
        return
    if event.sender_id == OWNER_ID or event.sender_id in DEV_USERS:
        pass
    else:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "LEGEND/modules/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.reply("Installed.... Ab Full Masti💥\n `{}`".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await event.reply("**Error!**\nCannot Install!\n Or Pre Installed Maybe..",
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            j = await event.reply(str(e))
            await asyncio.sleep(3)
            await j.delete()
            os.remove(downloaded_file_name)
    await asyncio.sleep(3)
    await event.delete()
__help__ = """
 *You can make a file 
  name. *

 ✪ /install for devs only 🙄
 ✪ /dox tag a message <file name> example /dox example.py

"""

__mod_name__ = "core 🙄"

