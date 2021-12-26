import pywhatkit as pw
from aiogram.types import ChatType, Message, CallbackQuery

from misc import dp
import Chats
from misc import bot
from aiogram import types


@dp.message_handler(chat_type=ChatType.PRIVATE, commands=['t2w'])
async def send_welcome(message: Message):
    Chats.User(message.from_user.id)
    text = """
    Tekst mantnini yuboring bizga :)
"""
    await message.reply(text, disable_web_page_preview=True, parse_mode="Html")
    

@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def T2W(message: types.Message):  # sourcery no-metrics
    await bot.send_chat_action(chat_id=message.from_user.id,action=types.ChatActions.TYPING)

    try:
        #check
        user=types.User.get_current()
        if message.text:
            await message.answer(f'<b>{message.text} - Rasm holatiga ugirilmoqda...</b>',parse_mode='html')
            await bot.send_chat_action(chat_id=message.from_user.id,action=types.ChatActions.UPLOAD_PHOTO)
            pw.text_to_handwriting(message.text,f"IMG/{user.full_name}.png",[0,0,138])
           
            await message.answer_photo(photo=open(f"IMG/{user.full_name}.png",'rb'),parse_mode="html")
          
    except Exception as e:
        await message.answer(e)
                
            
        