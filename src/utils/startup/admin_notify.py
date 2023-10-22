from emoji import emojize
from aiogram.types import BotCommand

from bot import bot
from utils.config import config


async def admin_notify():
    commands = [
        BotCommand(
            command="/start", description=emojize(":chequered_flag:Climb aboard!")
        ),
        BotCommand(command="/register", description=emojize(":handshake:Регистрация")),
        BotCommand(command="/menu", description=emojize(":house:Меню")),
    ]

    await bot.set_my_commands(commands)
    await bot.send_message(
        config.TG_ADMIN_CHAT_ID, "Бот перезапущен!", disable_notification=True
    )
