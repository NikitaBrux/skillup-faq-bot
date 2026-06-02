# SkillUp FAQ Bot

Telegram-бот для онлайн-школы **SkillUp** - отвечает на частые вопросы об обучении через inline-меню.

## Возможности

- Inline-меню с разделами: О школе, Цены, Обучение, Сертификат, FAQ
- Прямая ссылка на менеджера
- Кнопка «← Назад» для навигации
- Все тексты вынесены в `data/content.json` - легко редактировать без правки кода

## Стек

- Python 3.11+
- [aiogram 3](https://docs.aiogram.dev/) - асинхронный фреймворк для Telegram Bot API
- python-dotenv — управление переменными окружения

## Структура проекта

```
skillup-faq-bot/
├── bot.py               # Точка входа, polling
├── handlers/
│   ├── start.py         # /start и /help
│   └── faq.py           # Обработчики inline-кнопок
├── keyboards/
│   └── main_kb.py       # Главное меню и кнопка «Назад»
├── data/
│   └── content.json     # Тексты всех разделов
├── .env.example         # Шаблон переменных окружения
└── requirements.txt
```
