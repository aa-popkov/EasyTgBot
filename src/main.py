import asyncio
import logging
import sys
from typing import NamedTuple

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import config
from handlers import routes

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(config.TG_BOT_API_KEY, parse_mode=ParseMode.HTML)

async def main() -> None:
    from utils.startup import on_startup
    dp.startup.register(on_startup)

    dp.include_routers(*routes)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())