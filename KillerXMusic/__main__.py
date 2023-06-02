# credit @TeamKillerX
# by @xtsea

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from KillerXMusic import LOGGER, app, userbot
from KillerXMusic.core.call import KillerX
from KillerXMusic.plugins import ALL_MODULES
from KillerXMusic.utils.database import get_banned_users, get_gbanned

async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("KillerXMusic").error(
            "No Assistant Clients Vars Defined!.. Exiting Process."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("KillerXMusic").warning(
            "No Spotify Vars defined. Your bot won't be able to play spotify queries."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"KillerXMusic.plugins{all_module}")
    LOGGER("KillerXMusic.plugins").info(
        "Successfully Imported Modules "
    )
    await userbot.start()
    await KillerX.start()
    try:
        await KillerX.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("KillerXMusic").error(
            "[ERROR] - \n\nPlease turn on your Logger Group's Voice Call. Make sure you never close/end voice call in your log group"
        )
        sys.exit()
    except:
        pass
    await KillerX.decorators()
    LOGGER("KillerXMusic").info("KillerX Music Bot Started Successfully")
    await idle()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(init())
    LOGGER("KillerXMusic").info("Stopping KillerX Music Bot! GoodBye")
