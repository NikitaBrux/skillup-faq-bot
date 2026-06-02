from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from keyboards.main_kb import main_menu

router = Router()

WELCOME_TEXT = (
    "👋 Привет! Я FAQ-бот онлайн-школы <b>SkillUp</b>.\n\n"
    "Выбери раздел, чтобы узнать подробнее:"
)


@router.message(Command("start", "help"))
async def cmd_start(message: Message) -> None:
    await message.answer(WELCOME_TEXT, reply_markup=main_menu(), parse_mode="HTML")
