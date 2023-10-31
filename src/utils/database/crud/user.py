from sqlalchemy import select, delete, Result

from utils.database import db_helper
from models.users import User


async def create_user(user: User) -> bool:
    async with db_helper.session_factory() as session:
        try:
            session.add(user)
            await session.commit()
        except Exception as ex:
            # TODO: Add log with
            return False

        return True


async def get_user(tg_id: int) -> User | None:
    async with db_helper.session_factory() as session:
        stmt = select(User).where(User.tg_id == tg_id)
        user: User | None = await session.scalar(stmt)
        return user


async def get_all_users() -> list[User] | None:
    async with db_helper.session_factory() as session:
        stmt = select(User)
        users = await session.scalars(stmt)
        return [*users]


async def delete_user(tg_id: int) -> bool:
    async with db_helper.session_factory() as session:
        stmt = delete(User).where(User.tg_id == tg_id)
        result = await session.execute(stmt)
        await session.commit()
        return False if result.rowcount == 0 else True
