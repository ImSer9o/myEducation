import os
from os.path import join, dirname
import telebot

from dotenv import load_dotenv


def get_token_from_env(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


token = get_token_from_env('TG_BOT_TOKEN')
bot = telebot.TeleBot(token)

if __name__ == '__main__':
    bot.polling(none_stop=True)
