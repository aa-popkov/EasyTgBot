from typing import NamedTuple

import emoji


class AdminMenu(NamedTuple):
    get_all_users: str = emoji.emojize(":people_holding_hands: Дай всех юзеров")
    get_user_by_id: str = emoji.emojize(":man_construction_worker: Дай юзера по ID")
    delete_user_by_id: str = emoji.emojize(":warning: Удалить юзера по ID")
