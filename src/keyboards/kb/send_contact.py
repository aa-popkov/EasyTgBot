from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)

from keyboards.data import SendContact

btns = [
    [
        KeyboardButton(
            text=SendContact().text,
            request_contact=True,
        )
    ]
]
send_contact_kb = ReplyKeyboardMarkup(
    keyboard=btns, resize_keyboard=True, one_time_keyboard=True
)
