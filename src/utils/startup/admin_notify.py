from aiogram.types import BotCommand

from bot import bot
from config import config


async def admin_notify():
    commands = [
      BotCommand(command="/start", description="🏁Начать"),
      BotCommand(command="/menu", description="🏠Главное меню"),
    ]

    await bot.set_my_commands(commands)
    await bot.send_message(config.TG_ADMIN_CHAT_ID, "Бот перезапущен!\n/start", disable_notification=True)
