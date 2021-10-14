# NS Bots

import os
import logging
import pyrogram 
from info import BOT_TOKEN , API_ID , API_HASH


if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    NSBOTS = pyrogram.Client(
        "Caption_Editor",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        plugins=plugins,
        workers=300
    )
    NSBOTS.run()
