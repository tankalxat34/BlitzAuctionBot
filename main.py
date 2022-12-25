"""
Главный файл для бота

(c) tankalxat34 - 2022
"""

import telebot
import time
from telebot import types
import json

from backend import auction, dotenv, strings

_env = dotenv.DotEnv()
bot = telebot.TeleBot(_env.TOKEN)


with open("messages.json", "r", encoding="UTF-8") as file:
    messages = json.load(file)

auction = auction.Auction()


@bot.message_handler(content_types="text")
def all_messages(message):
    """Обработка всех входяих текстовых сообщений от пользователя"""
    user_id = message.from_user.id
    text = message.text
    command = message.text.lower()[1:]
    username = message.from_user.username

    if command in messages["commands"].keys():
        bot.send_message(user_id, strings.replaceAll(messages["commands"][command], {"%username%": username, "%time%": time.strftime("%d.%m.20%y %H:%M:%S")}), _env.PARSE_MODE)

        if command == "stat":
            bot.send_message(user_id, auction.str_available(), _env.PARSE_MODE)



print("Bot has beed started successfully!")
bot.infinity_polling()
