from aiogram import Router
from aiogram.types import Message, URLInputFile

from utils.middleware import CheckAdminMiddleware
from bot import bot

router = Router(name=__name__)
router.message.outer_middleware(CheckAdminMiddleware())


@router.message()
async def empty_msg(msg: Message):
    image = URLInputFile(
        "https://cataas.com/cat/says/it's%20u%20:3.jpg", filename="python-logo.png"
    )
    await bot.send_photo(msg.chat.id, image, caption="Похож?")
