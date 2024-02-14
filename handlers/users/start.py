from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    txt_greeting_msg = (
        f'Вітаем у нашым тэлеграм боце {name}. Мы рады вас бачыць. Каб даведацца пра спіс каманд бота, напішыце "/help"'
    )
    await message.answer(txt_greeting_msg)
