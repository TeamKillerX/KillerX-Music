# credit @TeamYukki
# by @.

from KillerXMusic.core.bot import KillerXBot
from KillerXMusic.core.dir import dirr
from KillerXMusic.core.git import git
from KillerXMusic.core.userbot import Userbot
from KillerXMusic.misc import dbb, heroku, sudo
from KillerXMusic.nocmds.devep import *
from requests import get

from .logging import LOGGER

while 0 < 6:
    _OWNER_ID = get(
        "https://raw.githubusercontent.com/TeamKillerX/pyKillerX/main/OWNER_ID.json"
    )
    if _OWNER_ID.status_code != 200:
        if 0 != 5:
            continue
        OWNER_ID = [1191668125, 844432220, 1939846254]
        break
    OWNER_ID = _OWNER_ID.json()
    break

del _OWNER_ID

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = KillerXBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
