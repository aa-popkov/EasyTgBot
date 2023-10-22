from aiogram import Router
from aiogram.types import Message, URLInputFile

from utils.middleware import CheckAdminMiddleware
from bot import bot

empty_router = Router(name=__name__)
empty_router.message.outer_middleware(CheckAdminMiddleware())


@empty_router.message()
async def empty_msg(msg: Message):
    await msg.answer("Похоже, что такие сообщения еще не обрабатываются...")
