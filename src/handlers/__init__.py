from aiogram import Router

from .empty import router as router_empty
from .start import router as router_start

routes: list[Router] = [
  router_start,
  router_empty, # ! Last Route
]

__all__ = [
  "routes"
]
