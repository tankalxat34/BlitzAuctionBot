"""
Главный файл для бота

(c) tankalxat34 - 2022
"""

# import telebot
# from telebot import types

from backend import dotenv

_env = dotenv.DotEnv()

print(_env.TOKEN)