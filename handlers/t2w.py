from contextvars import Context
import pywhatkit as pw
from aiogram.types import ChatType, Message, CallbackQuery
import time
from misc import dp
import Chats
from misc import bot
from aiogram import types
from config import TELEGRAM_TOKEN
import requests
import json

@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['t2w'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """
    Tekst mantnini yuboring bizga :)
"""
    await message.reply(text, disable_web_page_preview=True, parse_mode="Html")

# S2W
@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['S2W'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """
    Voice  yuboring bizga :)
"""
    await message.reply(text, disable_web_page_preview=True, parse_mode="Html")


#main code
@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def T2W(message: types.Message):  
    await bot.send_chat_action(chat_id=message.from_user.id,action=types.ChatActions.TYPING)

    try:
        #check
        user=types.User.get_current()
        
        if message.text:
            await message.answer(f'<b>{message.text} - Rasm holatiga ugirilmoqda...</b>',parse_mode='html')
            await bot.send_chat_action(chat_id=message.from_user.id,action=types.ChatActions.UPLOAD_PHOTO)
            pw.text_to_handwriting(message.text,f"IMG/{user.full_name}.png",[0,0,138])
           
            await message.answer_photo(photo=open(f"IMG/{user.full_name}.png",'rb'),parse_mode="html")
            
        else:
            await message.answer("Xatolik bor")
            
    except Exception as e:
        await message.answer(e)
                
            