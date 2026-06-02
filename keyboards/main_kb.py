import json
from pathlib import Path

from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

_content_path = Path(__file__).parent.parent / "data" / "content.json"
with _content_path.open(encoding="utf-8") as _f:
    _content = json.load(_f)


def main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="🏫 О школе", callback_data="faq_about")
    builder.button(text="💳 Цены и оплата", callback_data="faq_pricing")
    builder.button(text="📚 Как проходит обучение", callback_data="faq_process")
    builder.button(text="🎓 Сертификат", callback_data="faq_certificate")
    builder.button(text="❓ Частые вопросы", callback_data="faq_faq")
    builder.button(text="✍️ Написать менеджеру", url=_content["manager_url"])
    builder.adjust(2)
    return builder.as_markup()


def back_button() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text="← Назад", callback_data="faq_back")
    return builder.as_markup()
