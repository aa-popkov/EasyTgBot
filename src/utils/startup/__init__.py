from .admin_notify import admin_notify


async def on_startup():
  await admin_notify()


__all__ = [
  "on_startup"
]