from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Message

from utils.config import config


class CheckAdminMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        mgs_id = str(event.chat.id)
        if mgs_id == config.TG_ADMIN_CHAT_ID:
            return await handler(event, data)

        await event.answer(
            "Admin section! Not permited!\nGo to main menu: /menu", show_alert=True
        )

        return
