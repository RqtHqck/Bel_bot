from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import sqlite3
from loader import dp
from funcs.db_work.db_process import read_db
from data import config


@dp.message_handler(commands=['learn_word'])
async def bot_start(message: types.Message):
    """
    Эта функция нужна для учения* слов.
    Принцип: 
        . Берём РАНДОМНОЕ слово из db в таблице Words
        . Проверяем статус (true/false)
        . Отправляем его пользователю
        . Если слово уже изучено (true), выбрать другое и тд.
    """

    # -----Вызывается функция для того, чтобы взять новое слово из бд-----

    # Тут получаем рандомную строку 
    field_tuple = read_db(config.DB_NAME)
    print(field_tuple)
    rus = field_tuple[1]
    bel = field_tuple[2]


    await message.answer(text=f'Добра, вось ваша новае слова:\n {bel} - {rus}')
    