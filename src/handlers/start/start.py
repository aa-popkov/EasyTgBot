from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, URLInputFile

from bot import bot

router = Router(name=__name__)


@router.message(CommandStart())
async def cmd_start(msg: Message):
  await msg.answer("Welcome aboard!!")
