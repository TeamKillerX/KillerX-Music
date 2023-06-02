#
# Copyright (C) 2021-2022 by TeamKillerX@Github, < https://github.com/TeamKillerX >.
#
# This file is part of < https://github.com/TeamKillerX/KillerXMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamKillerX/KillerXMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pykeyboard import InlineKeyboard
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message

from config import BANNED_USERS
from strings import get_command, get_string
from KillerXMusic import app
from KillerXMusic.utils.database import get_lang, set_lang
from KillerXMusic.utils.decorators import (ActualAdminCB, language,
                                         languageCB)

# Languages Available


def lanuages_keyboard(_):
    keyboard = InlineKeyboard(row_width=2)
    keyboard.row(
        InlineKeyboardButton(
            text="🏴󠁧󠁢󠁥󠁮󠁧󠁿 English", callback_data="languages:en"
        ),
        InlineKeyboardButton(text="🇮🇳 हिन्दी", callback_data="languages:hi"),
    )
    keyboard.row(
        InlineKeyboardButton(text="🇱🇰 සිංහල", callback_data="languages:si"),
        InlineKeyboardButton(
            text="🇦🇿 Azərbaycan", callback_data="languages:az"
        ),
    )
    keyboard.row(
        InlineKeyboardButton(text="🇮🇳 ગુજરાતી", callback_data="languages:gu"),
        InlineKeyboardButton(
            text="🇹🇷 Türkiye Türkçesi", callback_data="languages:tr"
        ),
    )
    keyboard.row(
        InlineKeyboardButton(
            text="🐶 Cheems", callback_data="languages:cheems"
        ),
        InlineKeyboardButton(
            text="🇮🇩 Indonesian", callback_data="languages:id"
        ),
    )
    keyboard.row(
        InlineKeyboardButton(text="🇨🇴 Javenase", callback_data="languages:jw"),
        InlineKeyboardButton(
            text="🇬🇱 Sundanese", callback_data="languages:su"
        ),
    )
    keyboard.row(
        InlineKeyboardButton(text="🇩🇪 Jerman", callback_data="languages:jer"),
        InlineKeyboardButton(text="🇯🇵 Japan", callback_data="languages:jp"),
    )
    keyboard.row(
        InlineKeyboardButton(
            text=_["BACK_BUTTON"], callback_data="settingsback_helper"
        ),
        InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
    )
    return keyboard


LANGUAGE_COMMAND = get_command("LANGUAGE_COMMAND")


@app.on_message(
    filters.command(LANGUAGE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@language
async def langs_command(client, message: Message, _):
    keyboard = lanuages_keyboard(_)
    await message.reply_text(
        _["setting_1"].format(message.chat.title, message.chat.id),
        reply_markup=keyboard,
    )


@app.on_callback_query(filters.regex("LG") & ~BANNED_USERS)
@languageCB
async def lanuagecb(client, CallbackQuery, _):
    try:
        await CallbackQuery.answer()
    except:
        pass
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=keyboard
    )


@app.on_callback_query(
    filters.regex(r"languages:(.*?)") & ~BANNED_USERS
)
@ActualAdminCB
async def language_markup(client, CallbackQuery, _):
    langauge = (CallbackQuery.data).split(":")[1]
    old = await get_lang(CallbackQuery.message.chat.id)
    if str(old) == str(langauge):
        return await CallbackQuery.answer(
            "You're already on same language", show_alert=True
        )
    try:
        _ = get_string(langauge)
        await CallbackQuery.answer(
            "Successfully changed your language.", show_alert=True
        )
    except:
        return await CallbackQuery.answer(
            "Failed to change language or Language under update.",
            show_alert=True,
        )
    await set_lang(CallbackQuery.message.chat.id, langauge)
    keyboard = lanuages_keyboard(_)
    return await CallbackQuery.edit_message_reply_markup(
        reply_markup=keyboard
    )
