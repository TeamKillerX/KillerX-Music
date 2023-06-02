#
# Copyright (C) 2021-2022 by TeamKillerX@Github, < https://github.com/TeamKillerX >.
#
# This file is part of < https://github.com/TeamKillerX/KillerXMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamKillerX/KillerXMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from KillerXMusic import app


def back_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="TOPMARKUPGET",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def overallback_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GlobalStats",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def get_stats_markup(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_8"],
            callback_data="bot_stats_sudo g",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        ),
    ]
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SA_B_7"],
                    callback_data="TOPMARKUPGET",
                )
            ],
            [
                InlineKeyboardButton(
                    text=_["SA_B_6"],
                    url=f"https://t.me/{app.username}?start=stats",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_5"],
                    callback_data="TopOverall g",
                ),
            ],
            sudo if status else not_sudo,
        ]
    )


def stats_buttons(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["SA_B_5"],
            callback_data="TopOverall s",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["SA_B_8"],
            callback_data="bot_stats_sudo s",
        ),
        InlineKeyboardButton(
            text=_["SA_B_5"],
            callback_data="TopOverall s",
        ),
    ]
    return InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def back_stats_buttons(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GETSTATS",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )


def top_ten_stats_markup(_):
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["SA_B_2"],
                    callback_data="GetStatsNow Tracks",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_1"],
                    callback_data="GetStatsNow Chats",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["SA_B_3"],
                    callback_data="GetStatsNow Users",
                ),
                InlineKeyboardButton(
                    text=_["SA_B_4"],
                    callback_data="GetStatsNow Here",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GlobalStats",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
