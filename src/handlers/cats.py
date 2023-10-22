from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.types.input_file import URLInputFile

from keyboards.kb import main_menu_kb
from keyboards.data import MainMenu
from utils.states import Main
from utils.middleware import LongTimeMiddleware
from utils.enums import Flags
from bot import bot

cats_router = Router(name=__name__)
cats_router.message.middleware(LongTimeMiddleware())


@cats_router.message(F.text == MainMenu().cats, StateFilter(Main.main_state), flags={"key": Flags.LONG_OPERATION})
async def get_cats(msg: Message, state: FSMContext):
    await state.set_state(Main.cats_wait)
    cat_img = URLInputFile(
        url="https://cataas.com/cat",
        filename="some_file_name.jpg",
        timeout=5
    )
    await msg.reply_photo(photo=cat_img, reply_markup=main_menu_kb)
    await state.set_state(Main.main_state)


@cats_router.message(StateFilter(Main.cats_wait))
async def wait_cats(msg: Message):
    await msg.answer("Дождись предыдущих котов!")
