import asyncio

from aiogram import Bot, Dispatcher

from handlers import router#, send_notifications
from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    # asyncio.create_task(send_notifications(bot))
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    