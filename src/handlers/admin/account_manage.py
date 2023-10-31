from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, BufferedInputFile
from aiogram.filters import Command, StateFilter

from models.users import User
from utils.middleware import CheckAdminMiddleware
from keyboards.kb import admin_menu_users_kb
from keyboards.data import AdminMenuUsers
from utils.states import Main
from utils.database import get_user, delete_user, get_all_users
from bot import redis

acc_manage_router = Router(name=__name__)
