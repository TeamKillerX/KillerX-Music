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
from KillerXMusic.utils.database import is_muted, mute_on
from KillerXMusic.utils.decorators import AdminRightsCheck
from KillerXMusic.nocmds.prefix import command, other_filters

# Commands
# MUTE_COMMAND = get_command("MUTE_COMMAND")


@app.on_message(
    command(["mute", "cmute"])
    & other_filters
    & ~BANNED_USERS
)
@AdminRightsCheck
async def mute_admin(cli, message: Message, _, chat_id):
    if len(message.command) != 1 or message.reply_to_message:
        return await message.reply_text(_["general_2"])
    if await is_muted(chat_id):
        return await message.reply_text(_["admin_5"])
    await mute_on(chat_id)
    await KillerX.mute_stream(chat_id)
    await message.reply_text(
        _["admin_6"].format(message.from_user.mention)
    )
