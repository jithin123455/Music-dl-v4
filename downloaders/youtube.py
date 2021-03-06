from os import path

from yt_dlp import YoutubeDL

from config import BOT_NAME as bn, DURATION_LIMIT
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "verbose": True,
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"<b>π« ππΈπ³π΄πΎ πΈπ π»πΎπ½πΆπ΄π ππ·π°π½ {DURATION_LIMIT} πΌπΈπ½πππ΄π(π). ππ΄π½π³ ππ·πΎπππ΄π ππΎπ³π΄πΎ, π²π°π½'π πΏπ»π°π.πΏππΎππΈπ³π΄π³ ππΈπ³π΄πΎ πΈπ {duration} πΌπΈπ½πππ΄π(π)</b>"
        )

    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
