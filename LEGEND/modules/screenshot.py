# COPYRIGHT (C) BY LEGENDX2222 AND PROBOYX
"""
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
(((((((((((((((((((((((@LEGENDX2222)))))))))))))))))))))))))))
"""
import io
from LEGEND import telethn as borg
import requests
from LEGEND.events import register

SCREEN_SHOT_LAYER_ACCESS_KEY = "ed5c9f4f66729019d4a0ec6bdcabd5bd"
@register(pattern="^/sshot (.*)")
async def _(event):
    if event.fwd_from:
        return
    k = await event.reply("Painting Web_page...")
    sample_url = "https://api.screenshotlayer.com/api/capture?access_key={}&url={}&fullpage={}&viewport={}&format={}&force={}"
    input_str = event.pattern_match.group(1)
    response_api = requests.get(
        sample_url.format(
            SCREEN_SHOT_LAYER_ACCESS_KEY, input_str, "1", "2220x1080", "PNG", "1"
        )
    )
    lel = ("GRAND_OFFICIAL")
    # https://stackoverflow.com/a/23718458/4723940
    contentType = response_api.headers["content-type"]
    if "image" in contentType:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "GRANDBOT.png"
            try:
                await borg.send_file(
                    event.chat_id,
                    screenshot_image,
                    caption=lel,
                    force_document=True,
                    reply_to=event.message.reply_to_msg_id,
                )
                await k.delete()
                await event.delete()
            except Exception as e:
                await event.reply(str(e))
    else:
        await event.reply(response_api.text)
