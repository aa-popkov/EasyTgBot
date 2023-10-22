from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

from keyboards.data import AdminMenu

btn_data = AdminMenu()
btns = [
    [
        KeyboardButton(
            text=btn_data.get_all_users,
        ),
        KeyboardButton(
            text=btn_data.get_user_by_id,
        ),
    ],
    [
        KeyboardButton(
            text=btn_data.delete_user_by_id,
        ),
    ]
]

admin_menu_kb = ReplyKeyboardMarkup(
    keyboard=btns, resize_keyboard=True, one_time_keyboard=True
)
