from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(commands=['learn_word'])
async def bot_start(message: types.Message):
    # --Вызывается функция для того, чтобы взять новое слово из бд.
    
    
    
    await message.answer(text=f'Добра, вось ваша новае слова:')
    