from aiogram.fsm.state import StatesGroup, State


class Admin(StatesGroup):
    admin_menu = State()
    admin_menu_wait_user_id_get = State()
    admin_menu_wait_user_id_del = State()
