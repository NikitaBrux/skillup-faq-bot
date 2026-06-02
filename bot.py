import asyncio
import logging
from os import getenv

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers import faq, start

load_dotenv()

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    bot = Bot(token=getenv("BOT_TOKEN"))
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(faq.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
