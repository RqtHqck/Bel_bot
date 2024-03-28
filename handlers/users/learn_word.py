from aiogram import types
from loader import dp
from funcs.db_work.db_process import readDbWords
from data import config
from keyboards.inline.nextWord import nextWord
from aiogram.types import CallbackQuery
import logging
from funcs.db_work.takeWord import takeWord


# Получаем слово из бд


@dp.message_handler(commands=['learn_word'])
async def learn_words(message: types.Message):
    """
    Эта функция нужна для учения* слов.
    Принцип: 
        . Берём РАНДОМНОЕ слово из db в таблице Words? проверяя выучено ли оно (поле true/false)
        . Отправляем его пользователю
    """     
    # -----Вызывается функция для того, чтобы взять новое слово из бд-----

    # Тут получаем рандомную строку 
    translation = takeWord()
    if translation:
        logging.info(f'New word update {translation}')
    else:
        await message.answer(text=f'Вы вывучылі ўжо ўсе словы. Віншуем вас з гэтым. Вы прарабілі вялікую працу. Калі вы жадаеце дадаць новыя словы ў нашага бота, пішыце сюды:\n@RqtHqck')

    await message.answer(text=f'Добра, вось ваша новае слова:\n {translation[0]} - {translation[1]}', reply_markup=nextWord())


@dp.callback_query_handler(text='nextWord')
async def btn_next(callback: CallbackQuery):
    await callback.answer(cache_time=60)
    translation = takeWord()
    if translation:
        logging.info(f'New word update {translation}')
    else:
        await callback.message.answer(text=f'Вы вывучылі ўжо ўсе словы. Віншуем вас з гэтым. Вы прарабілі вялікую працу. Калі вы жадаеце дадаць новыя словы ў нашага бота, пішыце сюды:\n@RqtHqck')

    await callback.message.answer(text=f'Добра, вось ваша новае слова:\n {translation[0]} - {translation[1]}', reply_markup=nextWord())

@dp.callback_query_handler(text='cancelWordProcess')
async def btn_cancel(callback: CallbackQuery):
    await callback.answer(cache_time=60)
    await callback.message.delete()
    await callback.message.answer(text="Вы выйшлі. Выбярыце каманду для бота: /help")
    logging.info(msg=f"Exit from words learning")
