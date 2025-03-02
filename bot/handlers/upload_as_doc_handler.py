from pyrogram import Client, filters 
from pyrogram.types import Message
from bot import LOCAL, STATUS, COMMAND

@Client.on_message(filters.command(COMMAND.UPLOAD_AS_DOC))
async def func(client : Client, message: Message):
    STATUS.UPLOAD_AS_DOC = not STATUS.UPLOAD_AS_DOC
    await message.reply_text(LOCAL.UPLOAD_AS_DOC.format(status=STATUS.UPLOAD_AS_DOC))
