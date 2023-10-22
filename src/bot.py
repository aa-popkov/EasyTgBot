from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from redis.asyncio import client
from utils.config import config


r = client.Redis(password=config.REDIS_PASSWORD)
key_builder = DefaultKeyBuilder(
    prefix="user",
    separator=":",
    with_bot_id=True,
    with_destiny=True
)
dp = Dispatcher(storage=RedisStorage(r, key_builder))
bot = Bot(config.TG_BOT_API_KEY, parse_mode=ParseMode.HTML)
