from typing import NamedTuple

import emoji


class SendContact(NamedTuple):
    text: str = emoji.emojize(":mobile_phone_with_arrow: Отправить контакт")
