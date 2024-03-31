import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
import asyncio

load_dotenv()
bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()


@dp.message(F.text == "/start")
async  def start(message: Message):
    await message.reply("Hello")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
