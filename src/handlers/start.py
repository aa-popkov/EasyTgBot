from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from utils.database import get_user
from models.users import User
from utils.states import Register
from handlers.register import cmd_register
start_router = Router(name=__name__)


@start_router.message(CommandStart())
async def cmd_start(msg: Message, state: FSMContext):
    user_state = await state.get_state()
    user: User | None = await get_user(msg.from_user.id)
    if user_state and user:
        await msg.answer("Ты уже в системе...")
        return
    answer_msg = f"""Welcome aboard!\nДля начала давай пройдем регистрацию:\n/register"""
    await msg.answer(answer_msg)
    await state.set_state(Register.start_register)
    await cmd_register(msg, state)
