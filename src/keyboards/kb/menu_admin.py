from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from keyboards.data import AdminMenuUsers, AdminMenuAccount, AdminMenu

admin_menu_kb = ReplyKeyboardBuilder(
    markup=[[KeyboardButton(text=btn)] for btn in AdminMenu()],
).adjust(2).as_markup(resize_keyboard=True)

admin_menu_users_kb = ReplyKeyboardBuilder(
    markup=[[KeyboardButton(text=btn)] for btn in AdminMenuUsers()],
).adjust(2).as_markup(resize_keyboard=True)

admin_menu_budget_kb = ReplyKeyboardBuilder(
    markup=[[KeyboardButton(text=btn)] for btn in AdminMenuAccount()],
).adjust(2).as_markup(resize_keyboard=True)
