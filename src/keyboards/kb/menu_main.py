from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from keyboards.data import MainMenu

main_menu_kb = ReplyKeyboardBuilder(
    markup=[[KeyboardButton(text=btn)] for btn in MainMenu()],
).adjust(2).as_markup(resize_keyboard=True)
