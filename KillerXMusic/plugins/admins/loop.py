#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/KillerXMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/KillerXMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS
from strings import get_command
from KillerXMusic import app
from KillerXMusic.utils.database.memorydatabase import (get_loop,
                                                      set_loop)
from KillerXMusic.utils.decorators import AdminRightsCheck
from KillerXMusic.nocmds.prefix import command, other_filters

# Commands
# LOOP_COMMAND = get_command("LOOP_COMMAND")


@app.on_message(
    command(["loop", "cloop"])
    & other_filters
    & ~BANNED_USERS
)
@AdminRightsCheck
async def admins(cli, message: Message, _, chat_id):
    usage = _["admin_24"]
    if len(message.command) != 2:
        return await message.reply_text(usage)
    state = message.text.split(None, 1)[1].strip()
    if state.isnumeric():
        state = int(state)
        if not 1 <= state <= 10:
            return await message.reply_text(_["admin_26"])
        got = await get_loop(chat_id)
        if got != 0:
            state = got + state
        state = min(state, 10)
        await set_loop(chat_id, state)
        return await message.reply_text(
            _["admin_25"].format(
                message.from_user.first_name, state
            )
        )
    elif state.lower() == "enable":
        await set_loop(chat_id, 10)
        return await message.reply_text(
            _["admin_25"].format(message.from_user.first_name, state)
        )
    elif state.lower() == "disable":
        await set_loop(chat_id, 0)
        return await message.reply_text(_["admin_27"])
    else:
        return await message.reply_text(usage)
