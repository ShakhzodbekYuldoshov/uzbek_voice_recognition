from logging import basicConfig, ERROR

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TELEGRAM_TOKEN

bot = Bot(TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

basicConfig(level=ERROR)


def setup():
    #check is admin
    import filters
    filters.setup(dp)
    
    import handlers
    
    from utils import executor
    executor.setup()
