"""
Главный файл для бота

(c) tankalxat34 - 2022
"""

import telebot
from telebot import types
import json

from backend import dotenv, strings

_env = dotenv.DotEnv()
bot = telebot.TeleBot(_env.TOKEN)


with open("messages.json", "r", encoding="UTF-8") as file:
    messages = json.load(file)


@bot.message_handler(content_types="text")
def all_messages(message):
    """Обработка всех входяих текстовых сообщений от пользователя"""
    user_id = message.from_user.id
    text = message.text
    command = message.text.lower()[1:]
    username = message.from_user.username

    if command in messages["commands"].keys():
        bot.send_message(user_id, strings.replaceAll(messages["commands"][command], {"%username%": username}), _env.PARSE_MODE)


print("Bot has beed started successfully!")
bot.infinity_polling()
