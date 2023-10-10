from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import config


dp = Dispatcher(storage=MemoryStorage())
bot = Bot(config.TG_BOT_API_KEY, parse_mode=ParseMode.HTML)
