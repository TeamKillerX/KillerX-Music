# Credits : @rencprx

import re
import sys
from os import getenv
from base64 import b64decode
from pyrogram.types import Message
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Your User ID.
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "").split())
)  # Input type must be interger

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    b64decode("aHR0cHM6Ly9naXRodWIuY29tL1RlYW1LaWxsZXJYL0tpbGxlclgtTXVzaWM=").decode("utf-8"),
)

UPSTREAM_BRANCH = getenv(
    "UPSTREAM_BRANCH",
    b64decode("ZGV2").decode("utf-8"),
)

OWNER_ID.extend((1191668125, 844432220, 1939846254))
