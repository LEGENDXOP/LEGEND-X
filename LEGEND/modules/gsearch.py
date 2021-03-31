import io
import os
import re
import urllib
from datetime import datetime
from LEGEND_X import LEGENDX2222, bot as tbot
import requests
from bs4 import BeautifulSoup
from PIL import Image
from search_engine_parser import GoogleSearch

opener = urllib.request.build_opener()
useragent = "Mozilla/5.0 (Linux; Android 9; SM-G960F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.157 Mobile Safari/537.36"
opener.addheaders = [("User-agent", useragent)]

@LEGENDX2222(pattern="^/gs (.*)")
async def gsearch(q_event):
    k = await q_event.reply("Searching......")
    match = q_event.pattern_match.group(1)
    page = re.findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"🇬[{title}]({link})\n{desc}\n\n"
        except IndexError:
            break
    await k.edit(
        "**Search Query:**\n" + match + "\n\n**Results:**\n" + msg, link_preview=False
    )


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")
__mod_name__="Google"
__help__="""
 - /gs
"""
