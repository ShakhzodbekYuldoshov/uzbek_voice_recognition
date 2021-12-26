from misc import dp
import Chats
from misc import bot
from aiogram import types
import time

@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def S2W(message: types.Message):  # sourcery no-metrics
    await bot.send_chat_action(chat_id=message.from_user.id,action=types.ChatActions.TYPING)

    try:
        #check
        file_info =await bot.get_file(message.voice.file_id)
        downloaded_file = await message.voice.download('sava.wav')
        print(downloaded_file)
        await message.answer(f'<b> - audio holatiga ugirilmoqda...</b>',parse_mode='html')
        
        await bot.send_chat_action(chat_id=message.from_user.id,action=types.ChatActions.UPLOAD_AUDIO)
        voicesa = open(f'sava.wav', 'rb')
        await message.answer_audio(audio=voicesa)
        
            
    except Exception as e:
        await message.answer(e)
        
        