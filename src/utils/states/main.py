from aiogram.fsm.state import StatesGroup, State


class Main(StatesGroup):
    main_state = State()
    cats_wait = State()
