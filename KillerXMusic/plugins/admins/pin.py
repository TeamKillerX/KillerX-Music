# Credits : @rencprx 

from KillerXMusic import app
from KillerXMusic.nocmds.prefix import *

# pinned disabled notification 
@app.on_message(command("pin") & other_filters) 
def pin(bot, message):
    chatid = message.chat.id
    msgid = message.message_id
    app.pin_chat_message(chatid, msgid, disable_notification=True)
    await message.reply_text("Pinned successfully")
