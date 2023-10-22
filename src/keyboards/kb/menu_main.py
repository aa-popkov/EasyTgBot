from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

from keyboards.data import MainMenu

btn_data = MainMenu()
btns = [
    [
        KeyboardButton(
            text=btn_data.cats,
        ),

    ],
    [
        KeyboardButton(
            text=btn_data.info,
        ),
    ]
]

main_menu_kb = ReplyKeyboardMarkup(
    keyboard=btns, resize_keyboard=True, one_time_keyboard=True
)
