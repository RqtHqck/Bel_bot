from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
import sqlite3
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    txt_greeting_msg = (
        f'Вітаем у нашым тэлеграм боце {name}. Мы рады вас бачыць. Каб даведацца пра спіс каманд бота, напішыце "/help"'
    )
    def create_bd(DB_NAME):
        with sqlite3.connect(DB_NAME) as sql_connection:
            # Создали бд-запрос на создание таблицы courses сост. из 4-ёх колонок
            sql_request = """CREATE TABLE Words (
            ID INT PRIMARY KEY,
            Word VARCHAR(255) NOT NULL,
            Translation VARCHAR(255) NOT NULL,
            Used BOOLEAN DEFAULT FALSE
            );"""
            # Выполняем этот(sql_request) созданный запрос
            sql_connection.execute(sql_request)
    create_bd('sqlite3.db')
    await message.answer(txt_greeting_msg)
    