"""
Главный файл для бота

(c) tankalxat34 - 2022
"""

import telebot
import time
from telebot import types
import json

from backend import auction, dotenv, strings
import keyboards

_env = dotenv.DotEnv()
bot = telebot.TeleBot(_env.TOKEN)


with open("MESSAGES.json", "r", encoding="UTF-8") as file:
    MESSAGES = json.load(file)

auction = auction.Auction()


@bot.message_handler(content_types="text")
def all_MESSAGES(message):
    """Обработка всех входяих текстовых сообщений от пользователя"""
    user_id = message.from_user.id
    text = message.text
    command = message.text.lower()[1:]
    username = message.from_user.username

    if command in MESSAGES["commands"].keys():
        try:
            bot.send_message(user_id, strings.replaceAll(MESSAGES["commands"][command], {"%username%": username, "%time%": time.strftime("%d.%m.20%y %H:%M:%S")}), _env.PARSE_MODE, reply_markup=keyboards.KB_GET_AUCTION)
        except Exception:
            pass


    if text.lower() == "показать аукцион" or command == "stat":
        try:
            bot.send_message(user_id, auction.str_available(), _env.PARSE_MODE, reply_markup=keyboards.KB_OPEN_AUCTION)
        except Exception:
            bot.send_message(user_id, MESSAGES["texts"]["_error"], _env.PARSE_MODE)




print("Bot has beed started successfully!")
bot.infinity_polling()
