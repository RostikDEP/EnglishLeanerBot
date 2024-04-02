import bot
from bot import dp, dbProc
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class AddWord(StatesGroup):
    word = State()
    translate = State()
    sentence = State()


@dp.message(F.text == "/AddWord")
async def AddNewWord(message: Message, state: FSMContext):
    await state.set_state(AddWord.word)
    await message.answer("Введіть слово")


@dp.message(AddWord.word)
async def record_word(message: Message, state: FSMContext):
    await state.update_data(word=message.text)
    await state.set_state(AddWord.translate)
    await message.answer("Введіть переклад")


@dp.message(AddWord.translate)
async def record_translate(message: Message, state: FSMContext):
    await state.update_data(translate=message.text)
    await state.set_state(AddWord.sentence)
    await message.answer("Введіть приклад речення: ")


@dp.message(AddWord.sentence)
async def record_sentence(message: Message, state: FSMContext):
    await state.update_data(sentence=message.text)
    await message.answer("Чудово. Записую слово в базу..")
    data = await state.get_data()
    dbProc.AddWord(data['word'], data['translate'], data['sentence'], message.chat.id)
    await state.clear()