"""
#TODOO
CREDTIS : @RENCPRX 
DOT NOT REMOVE CREDITS
"""

from KillerXMusic import userbot as ass
from KillerXMusic import app
from KillerXMusic.nocmds.prefix import *

@app.on_message(command("asst_on") & other_filters) 
async def(asst_on, message):
    await ass.one.send_message(message.chat.id, "Assistant Online")
    # await ass.example.send_message(message.chat.id, "example") 


