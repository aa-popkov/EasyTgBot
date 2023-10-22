from typing import NamedTuple

import emoji


class MainMenu(NamedTuple):
    cats: str = emoji.emojize(":cat: Получить котика(-ов)")
    info: str = emoji.emojize(":help: Справка")
