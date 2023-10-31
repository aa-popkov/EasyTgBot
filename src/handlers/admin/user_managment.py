from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, BufferedInputFile
from aiogram.filters import Command, StateFilter

from models.users import User
from utils.middleware import CheckAdminMiddleware
from keyboards.kb import admin_menu_users_kb
from keyboards.data import AdminMenuUsers
from utils.states import Main, Admin
from utils.database import get_user, delete_user, get_all_users
from bot import redis

admin_user_router = Router(name=__name__)


@admin_user_router.message(F.text == AdminMenuUsers().get_user_by_id, StateFilter(Admin.admin_menu))
async def get_user_by_id_wait_msg(msg: Message, state: FSMContext):
    await state.set_state(Admin.admin_menu_wait_user_id_get)
    await msg.answer("Отправь TG ID", reply_markup=ReplyKeyboardRemove())


@admin_user_router.message(StateFilter(Admin.admin_menu_wait_user_id_get))
async def get_user_by_id_sent_msg(msg: Message, state: FSMContext):
    try:
        user_tgid = int(msg.text.strip())
    except ValueError as e:
        await msg.answer(f"Это не число!")
        return
    user: User | None = await get_user(user_tgid)
    if user:
        await msg.answer(f"Вот что мне удалось найти:\n{user}", reply_markup=admin_menu_users_kb)
    else:
        await msg.answer(f"Не нашел такого юзера", reply_markup=admin_menu_users_kb)
    await state.set_state(Admin.admin_menu)


@admin_user_router.message(F.text == AdminMenuUsers().delete_user_by_id, StateFilter(Admin.admin_menu))
async def del_user_by_id_wait_msg(msg: Message, state: FSMContext):
    await state.set_state(Admin.admin_menu_wait_user_id_del)
    await msg.answer("Отправь TG ID", reply_markup=ReplyKeyboardRemove())


@admin_user_router.message(StateFilter(Admin.admin_menu_wait_user_id_del))
async def del_user_by_id_msg(msg: Message, state: FSMContext):
    try:
        user_tgid = int(msg.text.strip())
    except ValueError as e:
        await msg.answer(f"Это не число!")
        return

    user: User | None = await delete_user(user_tgid)
    if not user:
        await msg.answer(f"Такой юзер не найден", reply_markup=admin_menu_users_kb)
    else:
        await msg.answer(f"Успешно удален", reply_markup=admin_menu_users_kb)
        async for redis_key in redis.scan_iter(f"fsm:{user_tgid}:*"):
            await redis.delete(redis_key)
    await state.set_state(Admin.admin_menu)


@admin_user_router.message(F.text == AdminMenuUsers().get_all_users, StateFilter(Admin.admin_menu))
async def get_all_users_msg(msg: Message, state: FSMContext):
    users = await get_all_users()
    if len(users) == 0:
        await msg.answer("Не нашлось пользователей")
        return
    file_users: bytes = b""
    for user in users:
        user_row = f"{user.tg_id} | {user.username}\n"
        file_users += bytes(user_row, "utf-8")
    text_file = BufferedInputFile(file_users, filename="file.txt")
    await msg.answer_document(text_file, caption="Список пользователей")
