from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import BigInteger, String, TIMESTAMP, Date

from models.systems import Base
from models.users import User
from utils.models import created_at, updated_at


class AccountType(Base):
    type: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    crated_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class AccountCategory(Base):
    title: Mapped[str]
    type_id: Mapped[int] = mapped_column(ForeignKey(AccountType.id), nullable=False)
    crated_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    def __str__(self):
        return self.title


class Account(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey(AccountCategory.id), nullable=False)
    type_id: Mapped[int] = mapped_column(ForeignKey(AccountType.id), nullable=False)
    date: Mapped[date] = mapped_column(Date(), nullable=False)
    crated_at: Mapped[created_at]
    updated_at: Mapped[updated_at]