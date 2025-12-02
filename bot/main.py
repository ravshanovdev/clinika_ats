import asyncio
from aiogram import Bot, Dispatcher
from bot.bot_config import BOT_TOKEN
import os
import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from bot.handlers.start import router


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    print('bot ishga tushdi...')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


