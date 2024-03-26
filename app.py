from aiogram import executor
import asyncio
from loader import dp
import middlewares, filters, handlers
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды


    await set_default_commands(dispatcher)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=dp.storage.close(), loop=loop, skip_updates=True)
