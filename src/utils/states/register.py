from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    start_register = State()
    wait_contact = State()
