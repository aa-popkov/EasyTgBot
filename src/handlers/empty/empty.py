from aiogram import Router, F
from aiogram.types import Message

from utils.middleware import CheckAdminMiddleware

router = Router(name=__name__)
router.message.outer_middleware(CheckAdminMiddleware())


@router.message()
async def empty_msg(msg: Message):
  await msg.answer("Unknow data")
