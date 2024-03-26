from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from funcs.db_work.db_process import readDbWords
from data import config
import logging



@dp.message_handler(commands=['learn_word'])
async def bot_start(message: types.Message):
    """
    Эта функция нужна для учения* слов.
    Принцип: 
        . Берём РАНДОМНОЕ слово из db в таблице Words? проверяя выучено ли оно (поле true/false)
        . Отправляем его пользователю
    """     
    # -----Вызывается функция для того, чтобы взять новое слово из бд-----

    # Тут получаем рандомную строку 
    
    field_tuple = readDbWords(config.DB_NAME_WORDS)
    if field_tuple:
        logging.info(f'New word update {field_tuple}')
        rus = field_tuple[1]
        bel = field_tuple[2]
    if field_tuple == False:
         await message.answer(text=f'Вы вывучылі ўжо ўсе словы. Віншуем вас з гэтым. Вы прарабілі вялікую працу. Калі вы жадаеце дадаць новыя словы ў нашага бота, пішыце сюды:\n@RqtHqck')



    await message.answer(text=f'Добра, вось ваша новае слова:\n {bel} - {rus}')
    