from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot import redis
empty_router = Router(name=__name__)


@empty_router.message()
async def empty_msg(msg: Message, state: FSMContext):
    await msg.answer("Похоже, что такие сообщения еще не обрабатываются...")
