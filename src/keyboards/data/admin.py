from typing import NamedTuple

import emoji


class AdminMenu(NamedTuple):
    users: str = "👨‍👩‍👧‍👦 Пользователи"
    budget: str = "💰 Бюджет"


class AdminMenuUsers(NamedTuple):
    get_all_users: str = "👨‍👩‍👧‍👦 Дай всех юзеров"
    get_user_by_id: str = "🙆 Дай юзера по ID"
    delete_user_by_id: str = "🚶 Удалить юзера по ID"


class AdminMenuAccount(NamedTuple):
    cats: str = "Категории"
    add_cat: str = "Добавить категорию"
    del_cat: str = "Удалить категорию категорию"
    get_all_cats: str = "Посмотреть все категорию"
    types: str = "Типы"
    add_type: str = "Добавить тип"
    del_type: str = "Удалить категорию тип"
    get_all_types: str = "Посмотреть все типы"
