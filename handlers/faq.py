import json
from pathlib import Path

from aiogram import Router
from aiogram.types import CallbackQuery

from keyboards.main_kb import back_button, main_menu

router = Router()

_data_path = Path(__file__).parent.parent / "data" / "content.json"
with _data_path.open(encoding="utf-8") as f:
    CONTENT: dict = json.load(f)

SECTION_KEYS = {
    "faq_about": "about",
    "faq_pricing": "pricing",
    "faq_process": "process",
    "faq_certificate": "certificate",
    "faq_faq": "faq",
}


@router.callback_query(lambda c: c.data in SECTION_KEYS)
async def handle_section(callback: CallbackQuery) -> None:
    key = SECTION_KEYS[callback.data]
    text = CONTENT.get(key, "Информация временно недоступна.")
    await callback.message.edit_text(text, reply_markup=back_button(), parse_mode="HTML")
    await callback.answer()


@router.callback_query(lambda c: c.data == "faq_back")
async def handle_back(callback: CallbackQuery) -> None:
    await callback.message.edit_text(
        "Выбери раздел:", reply_markup=main_menu()
    )
    await callback.answer()
