from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from keyboards.data import SendContact

send_contact_kb = ReplyKeyboardBuilder(
    markup=[[KeyboardButton(text=btn)] for btn in SendContact()],
).adjust(2).as_markup(resize_keyboard=True)
