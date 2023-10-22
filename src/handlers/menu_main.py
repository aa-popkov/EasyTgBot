from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.kb import main_menu_kb
from utils.states import Main

menu_main_router = Router(name=__name__)


@menu_main_router.message(Command("menu"))
async def cmd_start(msg: Message, state: FSMContext):
    await msg.answer(
        "Добро пожаловать в Главное Меню\n"
        "Весь доступный функционал доступен по кнопкам внизу\n"
        "Посмотреть справку: /help",
        reply_markup=main_menu_kb
    )
    await state.set_state(Main.main_state)
