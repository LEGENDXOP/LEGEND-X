# COPYRIGHT (C) 2021 BY LEGENDX2222 AND PROBOYX
# 1ST INLINE YOUTUBE PLUG-IN MADE BY LEGENDX2222 AND PROBOYX
# DONT KANG THIS
# IF YOU KANG THEN PLEASE TAKE PERMISSION
# ELSE READY FOR DMCA
"""
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
"""

# MADE BY LEGEND X AND PROBOY


from LEGEND_X import bot
import os
import re
import urllib
from math import ceil

import requests
from telethon import Button, custom, events, functions
from youtubesearchpython import SearchVideos

@bot.on(events.InlineQuery(pattern=r"yt (.*)"))
async def inline_id_handler(event: events.InlineQuery.Event):
    builder = event.builder
    k = event.pattern_match.group(1)
    if ";" in k:
         testinput,legendx = event.pattern_match.group(1).split(";")
    else:
         testinput = event.pattern_match.group(1)
         legendx = 5
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

__mod_name__="YouTube"
__help__ = """
 - `@grand50_bot yt <search your query> ;8`
    Use ; this as result stopper
"""
