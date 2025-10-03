import asyncio
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.enums import ParseMode
from config import TELEGRAM_BOT_TOKEN
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from bot.handlers import routers
from bot.middlewares.clear_state import AutoClearStateMiddleware

# инициализация объекта Бота с токеном и объявлением способа форматирования
bot = Bot(
    token=TELEGRAM_BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

# инициализация объекта Диспетчера с хранилищем
dp = Dispatcher(storage=MemoryStorage())

# главная асинхронная функция для запуска бота
async def main():
    # подключение всех роутеров
    dp.include_routers(*routers)

    dp.message.middleware(AutoClearStateMiddleware())

    try:
        # очистка обновлений для пропуска старых запросов в бота
        await bot.delete_webhook(drop_pending_updates=True)

        # запуск long polling
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        # корректное завершение сессии после остановки бота
        await bot.session.close()

# запуск
if __name__ == "__main__":
    asyncio.run(main())