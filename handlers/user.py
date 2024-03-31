from bot import dp
from aiogram import F
from  aiogram.types import Message


@dp.message(F.text == "/start")
async def welcome(message: Message):
    await           message.reply("Вітаю. Цей бот допоможе у вивченні англійських слів!")