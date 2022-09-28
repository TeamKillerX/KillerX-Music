# COMMAND PREFIX
```python
from KillerXMusic.nocmds.prefix import command, other_filters
from KillerXMusic import app

@app.on_message(command("example") & other_filters)
def spam(bot, message):
    app.send_photo(message.chat.id, "telegraph img links")
```
