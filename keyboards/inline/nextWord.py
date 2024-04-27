from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def nextWord():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
             [InlineKeyboardButton(text='Наступнае', callback_data='nextWord')],
            [InlineKeyboardButton(text='Адмяніць', callback_data='cancelWordProcess')]
        ], row_width=2
    )
    return keyboard
