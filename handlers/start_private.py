from aiogram.types import ChatType, Message, CallbackQuery

from misc import dp
import Chats


@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['start'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """
    Assalom alaykum botimizga hush kelibsiz
    
    /tthw
    /sthw
    /help
"""
    await message.reply(text, disable_web_page_preview=True, parse_mode="Html")

#help
@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['help'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """
    Unverseal bot! 
"""
    await message.reply(text, disable_web_page_preview=True, parse_mode="Html")