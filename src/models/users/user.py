from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import BigInteger, String, TIMESTAMP

from models.systems import Base
from utils.models import created_at, updated_at


class User(Base):
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str | None]
    phone: Mapped[str | None] = mapped_column(unique=True)
    crated_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    def __str__(self) -> str:
        return (f"tg_id: <a href=\"tg://user?id={self.tg_id}\">{self.tg_id}</a>\n"
                f"username: <a href=\"http://t.me/{self.username}\">@{self.username}</a>\n"
                f"phone: {self.phone}")
