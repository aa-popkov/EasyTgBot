from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from handlers.menu_main import menu_start

empty_router = Router(name=__name__)


@empty_router.message()
async def empty_msg(msg: Message, state: FSMContext):
    await msg.reply(
        "Похоже, что такие сообщения еще не обрабатываются...\n"
        "Возможно, логика бота нарушена.\n"
        "Перевожу в главное меню, попробуйте операцию снова\n"
        "\n"
        "/menu",
        reply_markup=ReplyKeyboardRemove()
    )
    await menu_start(msg, state)
