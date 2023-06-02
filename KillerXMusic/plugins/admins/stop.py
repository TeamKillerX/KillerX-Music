#
# Copyright (C) 2021-2022 by TeamKillerX@Github, < https://github.com/TeamKillerX >.
#
# This file is part of < https://github.com/TeamKillerX/KillerXMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamKillerX/KillerXMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from KillerXMusic import app
from KillerXMusic.core.call import KillerX
from KillerXMusic.utils.database import set_loop
from KillerXMusic.utils.decorators import AdminRightsCheck
from KillerXMusic.nocmds.prefix import command, other_filters

# Commands
# STOP_COMMAND = get_command("STOP_COMMAND")


@app.on_message(
    command(["stop", "end", "cstop", "cend"])
    & other_filters
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if len(message.command) != 1:
        return await message.reply_text(_["general_2"])
    await KillerX.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.mention)
    )
