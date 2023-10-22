from sqlalchemy.orm import Mapped

from models.systems import Base


class Answer(Base):
    text: Mapped[str]
    handler: Mapped[str | None]
