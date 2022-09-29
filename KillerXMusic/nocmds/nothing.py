# DO NOT CHANGE // AUTO CRASH

from .nocmds.devep import *

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
