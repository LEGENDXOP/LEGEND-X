# COPYRIGHT (C) 2021 BY LEGENDX22 AND PROBOYX
# 1ST INLINE YOUTUBE PLUG-IN MADE BY LEGENDX22 AND PROBOYX
# DONT KANG THIS
# IF YOU KANG THEN PLEASE TAKE PERMISSION
# ELSE READY FOR DMCA
"""
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX22)))))))))))))))))))))))))))
"""

# MADE BY LEGEND X AND PROBOY


from LEGENDX import bot as borg

from LEGENDX import bot as tgbot


import os
import re
import urllib
from math import ceil

import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import SearchVideos

@tgbot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    testinput,legendx = event.pattern_match.group(1).split(";")
    urllib.parse.quote_plus(testinput)
    lund = event.sender_id
    if lund == lund:
        results = []
        search = SearchVideos(f"{testinput}", offset=1, mode="dict", max_results=int(legendx))
        mi = search.result()
        moi = mi["search_result"]
        if search == None:
            resultm = builder.article(
                title="No Results.",
                description="Try Again With correct Spelling",
                text="**No Matching Found**",
                buttons=[
                    [Button.switch_inline("Search Again", query="yt ", same_peer=True)],
                ],
            )
            await event.answer([resultm])
            return
        for mio in moi:
            mo = mio["link"]
            thum = mio["title"]
            proboyx = mio["id"]
            thums = mio["channel"]
            td = mio["duration"]
            tw = mio["views"]
            kekme = f"https://img.youtube.com/vi/{proboyx}/hqdefault.jpg"
            okayz = f"**Title :** `{thum}` \n**Link :** {mo} \n**Channel :** `{thums}` \n**Views :** `{tw}` \n**Duration :** `{td}`"
            hmmkek = f"Channel : {thums} \nDuration : {td} \nViews : {tw}"
            results.append(
                await event.builder.article(
                    title=thum,
                    description=hmmkek,
                    text=okayz,
                    buttons=Button.switch_inline(
                        "Search Again", query="yt ", same_peer=True
                    ),
                )
            )
        await event.answer(results)

    if  lund == 1100231655:
        resultm = builder.article(title="me not your bot",description="Mind Your Business",text="Hey U Must Use https://github.com/LEGENDXOP/LEGEND-X  ",buttons=[[Button.switch_inline("Search Again", query="yt ", same_peer=True)],], )
        await event.answer([resultm])
        return

