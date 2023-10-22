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


async def delete_user(tg_id: int) -> bool:
    async with db_helper.session_factory() as session:
        stmt = delete(User).where(User.tg_id == tg_id)
        result: Result = await session.execute(stmt)
        await session.commit()
        return True