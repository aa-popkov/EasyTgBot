from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.filters import Command, StateFilter

from utils.middleware import CheckAdminMiddleware
from keyboards.kb import admin_menu_users_kb
from utils.states import Main, Admin
from .account_manage import acc_manage_router
from .user_managment import admin_user_router

admin_router = Router(name=__name__)
admin_router.message.middleware(CheckAdminMiddleware())
admin_router.sub_routers = [
    acc_manage_router,
    admin_user_router
]


@admin_router.message(Command("admin"), StateFilter(Main.main_state))
async def admin_menu_msg(msg: Message, state: FSMContext):
    await state.set_state(Admin.admin_menu)
    await msg.answer("Выбери нужное", reply_markup=admin_menu_users_kb)
