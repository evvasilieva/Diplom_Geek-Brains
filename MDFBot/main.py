import asyncio
from aiogram import Bot, Dispatcher # импорт 2х классивов
from app.handlers import router
from app.database.models import async_main

    
async def main():
    await async_main()
    bot = Bot(token='7020872196:AAERlgM3z8lt8aMeSNJ-KOxOM796_RHIg_A') # в этой переменной хранится бот
    dp = Dispatcher() 
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен!')



