from Zaid import app, API_ID, API_HASH
from config import ALIVE_PIC
from pyrogram import filters
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import * 

# © By itzshukla Your motherfucker if uh Don't gives credits.
@app.on_message(filters.command("clone"))
async def clone(bot: app, msg: Message):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n  /clone sᴇɴᴅ ʏᴏᴜʀ PʏʀᴏGʀᴀᴍ2 Sᴛʀɪɴɢ Sᴇssɪᴏɴ. ❤️")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("ʀᴜᴋᴏ ɴᴀ ᴍᴇʀɪ ᴊᴀᴀɴ...💌")
                   # change this Directry according to ur repo
        client = Client(name="Melody", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="Zaid/modules"))
        await client.start()
        user = await client.get_me()
        await msg.reply(f" 💘 ᴄʜɪʟʟ ʙᴀʙʏ ᴄʜɪʟ ❤️  {user.first_name} 💨.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
