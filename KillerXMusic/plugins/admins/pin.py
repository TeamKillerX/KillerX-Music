# Credits : @rencprx 

from KillerXMusic import app
from KillerXMusic.nocmds.prefix import *

# pinned disabled notification 
@app.on_message(command("pin") & other_filters) 
def pin(bot, message) -> str:
    chatid = message.chat.id
    msgid = msg.reply_to_message.message_id if msg.reply_to_message else msg.message_id
    if msg.chat.username:
        link_chat_id = msg.chat.username
        message_link = f"https://t.me/{link_chat_id}/{msgid}"
    elif (str(chatid)).startswith("-100"):
        link_chat_id = (str(chatid)).replace("-100", "")
        message_link = f"https://t.me/c/{link_chat_id}/{msgid}"
    app.pin_chat_message(chatid, msgid, disable_notification=True)
    await message.reply_text("Pinned successfully")
