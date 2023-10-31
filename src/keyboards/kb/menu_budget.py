from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from keyboards.data import BudgetMenu


budget_menu_kb = ReplyKeyboardBuilder(
    markup=[[KeyboardButton(text=btn)] for btn in BudgetMenu()],
).adjust(3).as_markup(resize_keyboard=True)
