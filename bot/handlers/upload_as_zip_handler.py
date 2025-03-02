from pyrogram import Client, filters 
from pyrogram.types import Message
from bot import LOCAL, STATUS, COMMAND

@Client.on_message(filters.command(COMMAND.UPLOAD_AS_ZIP))
async def func(client : Client, message: Message):
    STATUS.UPLOAD_AS_ZIP = not STATUS.UPLOAD_AS_ZIP
    await message.reply_text(LOCAL.UPLOAD_AS_ZIP.format(status=STATUS.UPLOAD_AS_ZIP))
