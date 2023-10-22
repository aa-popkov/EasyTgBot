from aiogram.fsm.state import StatesGroup, State


class Main(StatesGroup):
    main_state = State()
    cats_wait = State()
    admin_menu = State()
    admin_menu_wait_user_id_get = State()
    admin_menu_wait_user_id_del = State()
