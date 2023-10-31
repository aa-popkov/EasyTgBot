from sqlalchemy import select, delete

from utils.database import db_helper
from models.budget import Account, AccountCategory, AccountType


class AccountCategoryDb:
    @staticmethod
    async def create_category(cat: AccountCategory) -> bool:
        async with db_helper.session_factory() as session:
            try:
                session.add(cat)
                await session.commit()
            except Exception as ex:
                # TODO: Add log with
                return False

            return True

    @staticmethod
    async def get_category(cat_name: str) -> AccountCategory | None:
        async with db_helper.session_factory() as session:
            stmt = select(AccountCategory).where(AccountCategory.title == cat_name)
            cat: AccountCategory | None = await session.scalar(stmt)
            return cat

    @staticmethod
    async def get_all_category() -> list[AccountCategory] | None:
        async with db_helper.session_factory() as session:
            stmt = select(AccountCategory)
            cats = await session.scalars(stmt)
            return [*cats]

    @staticmethod
    async def delete_category(cat_name: str) -> bool:
        async with db_helper.session_factory() as session:
            stmt = delete(AccountCategory).where(AccountCategory.title == cat_name)
            result = await session.execute(stmt)
            await session.commit()
            return False if result.rowcount == 0 else True


class AccountTypeDb:
    @staticmethod
    async def create_type(typ: AccountType) -> bool:
        async with db_helper.session_factory() as session:
            try:
                session.add(typ)
                await session.commit()
            except Exception as ex:
                # TODO: Add log with
                return False

            return True

    @staticmethod
    async def get_type(type_name: str) -> AccountType | None:
        async with db_helper.session_factory() as session:
            stmt = select(AccountType).where(AccountType.type == type_name)
            typ: AccountType | None = await session.scalar(stmt)
            return typ

    @staticmethod
    async def get_all_type() -> list[AccountType] | None:
        async with db_helper.session_factory() as session:
            stmt = select(AccountType)
            types = await session.scalars(stmt)
            return [*types]

    @staticmethod
    async def delete_type(type_name: str) -> bool:
        async with db_helper.session_factory() as session:
            stmt = delete(AccountType).where(AccountType.type == type_name)
            result = await session.execute(stmt)
            await session.commit()
            return False if result.rowcount == 0 else True


class AccountDb:
    @staticmethod
    async def create_account(acc: Account) -> bool:
        async with db_helper.session_factory() as session:
            try:
                session.add(acc)
                await session.commit()
            except Exception as ex:
                # TODO: Add log with
                return False

            return True

    @staticmethod
    async def get_account(acc_id: int) -> Account | None:
        async with db_helper.session_factory() as session:
            stmt = select(Account).where(Account.id == acc_id)
            acc: Account | None = await session.scalar(stmt)
            return acc

    @staticmethod
    async def get_all_account() -> list[Account] | None:
        async with db_helper.session_factory() as session:
            stmt = select(Account)
            accs = await session.scalars(stmt)
            return [*accs]

    @staticmethod
    async def delete_account(acc_id: int) -> bool:
        async with db_helper.session_factory() as session:
            stmt = delete(Account).where(Account.id == acc_id)
            result = await session.execute(stmt)
            await session.commit()
            return False if result.rowcount == 0 else True
