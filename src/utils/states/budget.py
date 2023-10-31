from aiogram.fsm.state import StatesGroup, State


class Budget(StatesGroup):
    main_state = State()
    balance = State()
    accounting = State()
    report = State()
    settings = State()
