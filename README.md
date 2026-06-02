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

## Запуск локально

**1. Клонируй репозиторий**

```bash
git clone https://github.com/твой_ник/skillup-faq-bot.git
cd skillup-faq-bot
```

**2. Установи зависимости**

```bash
pip install -r requirements.txt
```

**3. Создай `.env` и добавь токен**

```bash
cp .env.example .env
```

Получи токен у [@BotFather](https://t.me/BotFather) и вставь в `.env`:

```
BOT_TOKEN=your_token_here
```

**4. Запусти**

```bash
python3 bot.py
```

## Деплой

Бот готов к деплою на [Railway](https://railway.app) — достаточно подключить репозиторий и добавить переменную `BOT_TOKEN` в настройках окружения.

## Лицензия

MIT
