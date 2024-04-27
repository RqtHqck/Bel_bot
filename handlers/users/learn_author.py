from aiogram import types
from loader import dp, bot
from data import config
from aiogram.types import CallbackQuery, InlineKeyboardButton
from keyboards.inline.authorsSwithing import swithcerAll, swithcerPrevious
from funcs.db_work.db_process import readDbAuthors
import requests
import re

import logging
class ImageDomnloader:
    def __init__(self):
        self.number = 0

    def inc(self):
        self.number += 1


image = ImageDomnloader()


class Page:
    def __init__(self):
        self.status = 0

    def upvoteStatus(self):
        self.status += 5

    def devoteStatus(self):
        self.status -= 5


page = Page()


# Получаем все важные значения из словаря для дальнейшего обращения
allAuthorsDict = readDbAuthors(config.DB_NAME_AUTHORS, 'authors')
allAuthorsValues = list(allAuthorsDict.values())
allAuthorsNames = []
# Список имён
i = 0
for item in allAuthorsValues:
    name = allAuthorsValues[i][0].replace('\n', '')  # заменяем символ новой строки на пустую строку
    allAuthorsNames.append(name)
    i += 1
lengthAuthors = len(allAuthorsNames)
i=0

# CURRENT PAGE
@dp.message_handler(commands=['learn_authors'])
async def learnAuthors(message: types.Message):
    currentAuthorsNames = []
    pages = []
    page.upvoteStatus()

    for i in range (0, page.status):
        currentAuthorsNames.append(allAuthorsNames[i])

    swithcerAll = types.InlineKeyboardMarkup(row_width=2)
    for author in currentAuthorsNames:
        button = types.InlineKeyboardButton(text=f"{author}", callback_data=f'author_{author}')
        swithcerAll.add(button)

    swithcerAll.add(InlineKeyboardButton(text='Папярэднія', callback_data='prev'),
                     InlineKeyboardButton(text='Наступныя', callback_data='next'))
    swithcerAll.add(InlineKeyboardButton(text='Адмяніць', callback_data='cancel'))

    fstring = f'У нас ёсць наступныя аўтары:'

    await message.answer(text=fstring,
                         reply_markup=swithcerAll)

    logging.info(msg=f"Command 'learn_authors' clicked in start-mode. pages = [{pages}], pageStatus = {page.status}")

    currentAuthorsNames.clear()
    pages.clear()


# NEXT BUTTON
@dp.callback_query_handler(text='next')
async def btn_next(callback: CallbackQuery):
    # Hide the watches near the message if button was pressed
    await callback.answer(cache_time=60)
    currentAuthorsNames = []
    pages = []
    page.upvoteStatus()
    if page.status == lengthAuthors:
        for i in range(page.status - 5, page.status):
            currentAuthorsNames.append(allAuthorsNames[i])

        swithcerPrevious = types.InlineKeyboardMarkup(row_width=2)
        for author in currentAuthorsNames:
            button = types.InlineKeyboardButton(text=f"{author}", callback_data=f'author_{author}')
            swithcerPrevious.add(button)
        swithcerPrevious.add(InlineKeyboardButton(text='Папярэднія', callback_data='prev'))
        swithcerPrevious.add(InlineKeyboardButton(text='Адмяніць', callback_data='cancel'))

        fstring = f'У нас ёсць наступныя аўтары:'
        await callback.message.delete()
        await callback.message.answer(
            text=fstring,
            reply_markup=swithcerPrevious)
        logging.info(
            msg=f"Command 'learn_authors' clicked in start-mode. pages = [{pages}], pageStatus = {page.status}")

    else:
        for i in range(page.status - 5, page.status):
            currentAuthorsNames.append(allAuthorsNames[i])

        swithcerAll = types.InlineKeyboardMarkup(row_width=2)
        for author in currentAuthorsNames:
            button = types.InlineKeyboardButton(text=f"{author}", callback_data=f'author_{author}')
            swithcerAll.add(button)

        swithcerAll.add(InlineKeyboardButton(text='Папярэднія', callback_data='prev'),
                        InlineKeyboardButton(text='Наступныя', callback_data='next'))
        swithcerAll.add(InlineKeyboardButton(text='Адмяніць', callback_data='cancel'))

        fstring = f'У нас ёсць наступныя аўтары:'
        await callback.message.delete()
        await callback.message.answer(
            text=fstring,
            reply_markup=swithcerAll)
        logging.info(
            msg=f"Command 'learn_authors' clicked in start-mode. pages = [{pages}], pageStatus = {page.status}")

    currentAuthorsNames.clear()
    pages.clear()


# PREVIOUS BUTTON
# ==============================================================================
@dp.callback_query_handler(text='prev')
async def btn_prev(callback: CallbackQuery):
    # Hide the watches near the message if button was pressed
    await callback.answer(cache_time=60)
    currentAuthorsNames = []
    pages = []
    page.devoteStatus()
    # СОЗДАНИЕ СПИСКА АВТОРОВ
    if page.status == 5:
        for i in range(page.status - 5, page.status):
            currentAuthorsNames.append(allAuthorsNames[i])
        # СОЗДАЁМ ДИНАМИЧЕСКУЮ ИНЛАЙН КЛАВИАТУРУ
        swithcerNext = types.InlineKeyboardMarkup(row_width=2)
        for author in currentAuthorsNames:
            button = types.InlineKeyboardButton(text=f"{author}", callback_data=f'author_{author}')
            swithcerNext.add(button)
        swithcerNext.add(InlineKeyboardButton(text='Наступныя', callback_data='next'))
        swithcerNext.add(InlineKeyboardButton(text='Адмяніць', callback_data='cancel'))
        # ОТПРАВКА СООБЩЕНИЯ
        fstring = f'У нас ёсць наступныя аўтары:'
        await callback.message.delete()
        await callback.message.answer(
            text=fstring,
            reply_markup=swithcerNext)
        logging.info(
            msg=f"Command 'learn_authors' clicked in start-mode. pages = [{pages}], pageStatus = {page.status}")

    else:
        for i in range(page.status - 5, page.status):
            currentAuthorsNames.append(allAuthorsNames[i])

        swithcerAll = types.InlineKeyboardMarkup(row_width=2)
        for author in currentAuthorsNames:
            button = types.InlineKeyboardButton(text=f"{author}", callback_data=f'author_{author}')
            swithcerAll.add(button)

        swithcerAll.add(InlineKeyboardButton(text='Папярэднія', callback_data='prev'),
                        InlineKeyboardButton(text='Наступныя', callback_data='next'))
        swithcerAll.add(InlineKeyboardButton(text='Адмяніць', callback_data='cancel'))


        fstring = f'У нас ёсць наступныя аўтары:'
        await callback.message.delete()
        await callback.message.answer(
            text=fstring,
            reply_markup=swithcerAll)
        logging.info(msg=f"Command 'learn_authors' clicked in start-mode.Ц pages = [{pages}], pageStatus = {page.status}")

    currentAuthorsNames.clear()
    pages.clear()


# CANCEL BUTTON
# ==============================================================================
@dp.callback_query_handler(text='cancel')
async def btn_cancel(callback: CallbackQuery):
    await callback.answer(cache_time=60)
    currentAuthorsNames = []
    pages = []
    page.status = 0
    await callback.message.delete()
    await callback.message.answer(text="Вы выйшлі. Выбярыце каманду для бота: /help")
    logging.info(msg=f"Button 'cancel' clicked. pages = [{pages}], pageStatus = {page.status}")


# AUTHOR BUTTON
# ==============================================================================
@dp.callback_query_handler(lambda c: re.match(r'author_', c.data))
async def btn_author(callback:CallbackQuery):

    await callback.answer(cache_time=60)

    # ПОЛУЧАЕМ ID АВТОРА
    authorName = callback.data.split('_')[1]
    logging.info(msg=f"Chosed author: {authorName}")
    authorId = 0
    for i in range(0, lengthAuthors):
        if authorName == allAuthorsNames[i]:
            authorId = i+1
            break

    # ЧТЕНИЕ ДАННЫХ ПО КЛЮЧУ
    findedAuthorData = readDbAuthors(config.DB_NAME_AUTHORS, 'authors', authorId)

    # ОЧИСТКА ПОЛУЧЕННЫХ ДАННЫХ
    clearAuthorData = []
    for item in findedAuthorData[:-1]:
        name = item.replace('\n', '')
        clearAuthorData.append(name)
    # СКАЧИВАЕМ КАРИТНКУ
    def download_image(url, filepath):
        response = requests.get(url)
        with open(filepath, 'wb') as file:
            file.write(response.content)

    # КЛЮЧЕВЫЕ ЗНАЧЕНИЯ ПОЛУЧЕННЫХ ДАННЫХ
    name = clearAuthorData[0]
    bioText = clearAuthorData[2]
    compositions = clearAuthorData[1]
    imageUrl = clearAuthorData[-2]
    wikiUrl = clearAuthorData[-1]


    download_image(imageUrl, f'/home/rqthqck/programFiles/Python/BOTS/Aiogram/bel_bot/images/my_image{image.number}')

    # ОТПРАВКА ДАННЫХ ПОЛЬЗОВАТЕЛЮ
    await bot.send_photo(chat_id=callback.from_user.id,
                         photo=imageUrl,
                         caption=f"<b>{name}</b>\n{bioText}\n<b>Творы аўтара:</b>\n {compositions}\n\n<b>Каб даведацца больш, пераходзіце па спасылцы на вікіпедыю:</b>\n{wikiUrl}",
                         parse_mode='HTML')




    logging.info(msg=f"Button with callback='{callback.data}' was clicked.")