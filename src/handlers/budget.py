from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from keyboards.kb import budget_menu_kb
from keyboards.data import MainMenu
from utils.states import Budget, Main

menu_budget_router = Router(name=__name__)


@menu_budget_router.message(Command("budget"), StateFilter(Main.main_state))
@menu_budget_router.message(F.text == MainMenu().budget, StateFilter(Main.main_state))
async def budget_menu(msg: Message, state: FSMContext):
    await msg.answer(
        "Меню управление Бюджетом",
        reply_markup=budget_menu_kb
    )
    await state.set_state(Budget.main_state)
