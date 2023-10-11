from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
  tg_id: Mapped[str]
  username: Mapped[Optional[str]]
  bio: Mapped[Optional[str]]

