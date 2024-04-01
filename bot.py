import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
import asyncio
from database import dbProcessor


load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()
dbProc = dbProcessor("data/words.db")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    from handlers import *
    asyncio.run(main())
