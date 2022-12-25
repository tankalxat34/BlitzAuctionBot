"""
Все клавиатуры для чат-бота

(c) tankalxat34 - 2022
"""

from telebot import types

KB_OPEN_AUCTION = types.InlineKeyboardMarkup([
        [types.InlineKeyboardButton(text='Открыть аукцион', url='https://tanksblitz.ru/ru/auction/')],
        # [types.InlineKeyboardButton(text='on Telegram', url='https://t.me')],
    ])


KB_GET_AUCTION = types.ReplyKeyboardMarkup(True, one_time_keyboard=False)
KB_GET_AUCTION.add(types.KeyboardButton("Показать аукцион"))