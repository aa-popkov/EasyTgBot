import asyncio
import logging
import sys
from typing import NamedTuple

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot import dp, bot
from utils.startup import on_startup
from handlers import routes


async def main() -> None:
    dp.startup.register(on_startup)
    dp.include_routers(*routes)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    asyncio.run(main())