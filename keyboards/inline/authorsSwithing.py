from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def swithcerAll(authorsList):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Папярэднія', callback_data='prev'),
             InlineKeyboardButton(text='Наступныя', callback_data='next')],

            [InlineKeyboardButton(text=f"{authorsList[0]}", callback_data=f'author_{authorsList[0]}'),
             InlineKeyboardButton(text=f"{authorsList[1]}", callback_data=f'author_{authorsList[1]}')],
             [InlineKeyboardButton(text=f"{authorsList[2]}", callback_data=f'author_{authorsList[2]}'),
             InlineKeyboardButton(text=f"{authorsList[3]}", callback_data=f'author_{authorsList[3]}')],
             [InlineKeyboardButton(text=f"{authorsList[4]}", callback_data=f'author_{authorsList[4]}')],

            [InlineKeyboardButton(text='Адмяніць', callback_data='cancel')]
        ], row_width=2
    )
    return keyboard

def swithcerNext(authorsList):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
             [InlineKeyboardButton(text='Наступныя', callback_data='next')],

            [InlineKeyboardButton(text=f"{authorsList[0]}", callback_data=f'author_{authorsList[0]}'),
             InlineKeyboardButton(text=f"{authorsList[1]}", callback_data=f'author_{authorsList[1]}')],
             [InlineKeyboardButton(text=f"{authorsList[2]}", callback_data=f'author_{authorsList[2]}'),
             InlineKeyboardButton(text=f"{authorsList[3]}", callback_data=f'author_{authorsList[3]}')],
             [InlineKeyboardButton(text=f"{authorsList[4]}", callback_data=f'author_{authorsList[4]}')],

            [InlineKeyboardButton(text='Адмяніць', callback_data='cancel')]
        ], row_width=2
    )
    return keyboard

def swithcerPrevious(authorsList):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Папярэднія', callback_data='prev')],

            [InlineKeyboardButton(text=f"{authorsList[0]}", callback_data=f'author_{authorsList[0]}'),
             InlineKeyboardButton(text=f"{authorsList[1]}", callback_data=f'author_{authorsList[1]}')],
             [InlineKeyboardButton(text=f"{authorsList[2]}", callback_data=f'author_{authorsList[2]}'),
             InlineKeyboardButton(text=f"{authorsList[3]}", callback_data=f'author_{authorsList[3]}')],
             [InlineKeyboardButton(text=f"{authorsList[4]}", callback_data=f'author_{authorsList[4]}')],

            [InlineKeyboardButton(text='Адмяніць', callback_data='cancel')]
        ], row_width=2
    )
    return keyboard