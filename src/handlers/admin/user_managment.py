from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, StateFilter

from models.users import User
from utils.middleware import CheckAdminMiddleware
from keyboards.kb import admin_menu_kb
from keyboards.data import AdminMenu
from utils.states import Main
from utils.database import get_user, delete_user
from bot import redis

admin_router = Router(name=__name__)
admin_router.message.middleware(CheckAdminMiddleware())


@admin_router.message(Command("admin"), StateFilter(Main.main_state))
async def admin_menu_msg(msg: Message, state: FSMContext):
    await state.set_state(Main.admin_menu)
    await msg.answer("Выбери нужное", reply_markup=admin_menu_kb)


@admin_router.message(F.text == AdminMenu().get_user_by_id, StateFilter(Main.admin_menu))
async def get_user_by_id_wait_msg(msg: Message, state: FSMContext):
    await state.set_state(Main.admin_menu_wait_user_id_get)
    await msg.answer("Отправь TG ID", reply_markup=ReplyKeyboardRemove())


@admin_router.message(StateFilter(Main.admin_menu_wait_user_id_get))
async def get_user_by_id_sent_msg(msg: Message, state: FSMContext):
    try:
        user_tgid = int(msg.text.strip())
    except ValueError as e:
        await msg.answer(f"Это не число!")
        return
    user: User | None = await get_user(user_tgid)
    if user:
        await msg.answer(f"Вот что мне удалось найти:\n{user}", reply_markup=admin_menu_kb)
    else:
        await msg.answer(f"Не нашел такого юзера", reply_markup=admin_menu_kb)
    await state.set_state(Main.admin_menu)


@admin_router.message(F.text == AdminMenu().delete_user_by_id, StateFilter(Main.admin_menu))
async def del_user_by_id_wait_msg(msg: Message, state: FSMContext):
    await state.set_state(Main.admin_menu_wait_user_id_del)
    await msg.answer("Отправь TG ID", reply_markup=ReplyKeyboardRemove())


@admin_router.message(StateFilter(Main.admin_menu_wait_user_id_del))
async def del_user_by_id_msg(msg: Message, state: FSMContext):
    try:
        user_tgid = int(msg.text.strip())
    except ValueError as e:
        await msg.answer(f"Это не число!")
        return
    
    user: User | None = await delete_user(user_tgid)
    if not user:
        await msg.answer(f"Такой юзер не найден", reply_markup=admin_menu_kb)
    else:
        await msg.answer(f"Успешно удален", reply_markup=admin_menu_kb)
        async for redis_key in redis.scan_iter(f"fsm:{user_tgid}:*"):
            await redis.delete(redis_key)
    await state.set_state(Main.admin_menu)
