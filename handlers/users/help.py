from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Спіс каманд: ",
            "/start - Пачаць дыялог",
            "/help - Атрымаць даведку",
            "/quest - Пачаць квэст апытанне")
    
    await message.answer("\n".join(text))
