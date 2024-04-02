import bot
from bot import dp, dbProc
from aiogram import F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from fuzzywuzzy import fuzz


class StartLearn(StatesGroup):
    get_answer = State()
    translate = State()     #I will use MEMORY in future
    sentence = State()
    mode = State()


@dp.message(F.text == "/StartLearn")
async def StartLearnWords(message: Message, state: FSMContext):
    await state.set_state(StartLearn.get_answer)
    word = dbProc.GetRandomWord()
    await state.update_data(translate=word[2])
    await state.update_data(sentence=word[3])
    await message.answer(f"Введи переклад: {word[1]}")


@dp.message(StartLearn.get_answer)
async def GetAnswer(message: Message, state: FSMContext):
    if "/stop" in message.text:
        await state.clear()
        await message.answer("Навчання зупинене!😉")
        return
    data = await state.get_data()

    if fuzz.ratio(message.text, data['translate']) > 80:
        await message.answer("Правильно!✅")
    else:
        await message.answer(f"Не правильно!❌ Правильний переклад: {data['translate']}")
    await message.answer(data['sentence'])

    await state.clear()
    await StartLearnWords(message, state)


