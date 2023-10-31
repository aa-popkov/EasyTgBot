from aiogram import Router, F
from aiogram.enums.content_type import ContentType
from aiogram.filters import Command, StateFilter, and_f
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,
)

from utils.states import Register, Main
from utils.database import get_user, create_user
from models.users import User
from keyboards.kb import main_menu_kb, send_contact_kb

register_router = Router(name=__name__)


@register_router.message(Command("register"))
@register_router.message(StateFilter(Register.start_register))
async def cmd_register(msg: Message, state: FSMContext):
    user: User | None = await get_user(msg.from_user.id)
    if user:
        await msg.answer(
            "Ты уже зергистрирован, со следующими параметрами:\n"
            f"{user}\n"
            f"\n"
            "Перевожу в главное /menu",
            reply_markup=main_menu_kb,
            disable_web_page_preview=True
        )
        await state.set_state(Main.main_state)
        return

    await msg.answer(
        "Отправьте свой контакт для завершения регистрации",
        reply_markup=send_contact_kb,
    )
    await state.set_state(Register.wait_contact)


@register_router.message(
    StateFilter(Register.wait_contact), F.content_type == ContentType.CONTACT
)
async def cmd_register_get_contact(msg: Message, state: FSMContext):
    """
    Принимает запросы в статус wait_contact, типа контакт
    """
    if msg.contact.user_id != msg.from_user.id:
        await msg.answer(
            "Это чужой контакт!\n"
            "Попробуй еще раз, хитрая жопа",
            reply_markup=main_menu_kb,
        )
        return

    user: User = User()
    user.tg_id = msg.from_user.id
    user.phone = msg.contact.phone_number
    user.username = msg.from_user.username

    create_user_result = await create_user(user)
    if not create_user_result:
        await msg.answer("Не удалось завершить регистрацию")
        return

    await msg.answer(
        "Регистрация успешно заверешна!\n"
        "Можешь переходить в /menu",
        reply_markup=ReplyKeyboardRemove(),
    )

    await state.set_state(Main.main_state)


@register_router.message(
    StateFilter(Register.wait_contact), F.content_type != ContentType.CONTACT
)
async def cmd_register_not_contact(msg: Message, state: FSMContext):
    await msg.answer("Необходимо отправить свой контакт по кнопке\n"
                     "Без этого я не смогу завершить регистрацию",
                     reply_markup=send_contact_kb)
