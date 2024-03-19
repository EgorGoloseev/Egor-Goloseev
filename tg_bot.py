import os
import random

import telebot
from dotenv import load_dotern

load_dotern()

token = os.getenv()

bot = telebot.Telebot(token)


@bot.message_handler(commands=['start','help'])
def handler_start(message):
    bot.send_message(message.chat.id,   'привет я бот.\n'
                     'Используй команду: /users.')

@bot.message_handler(commands=['users'])
def handler_users(message):
    url = f'https://jsonplaceholder.typicode.com/users{random.randint(1,10)}'
    response = requests.get(url)
    if response.status_code ==200:
        users = response.json()
        print(users)

bot.polling(none_stop=True)