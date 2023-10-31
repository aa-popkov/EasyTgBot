from aiogram import Router

from .start import start_router
from .register import register_router
from .empty import empty_router
from .admin import admin_router
from .menu_main import menu_main_router
from .cats import cats_router
from .budget import menu_budget_router

routes: list[Router] = [
    menu_budget_router,
    cats_router,
    menu_main_router,
    start_router,
    admin_router,
    register_router,
    empty_router,  # ! Last Route
]

__all__ = ["routes"]
