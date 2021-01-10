import telebot
import json
import requests
from config import TOKEN, currency
from extensions import Converter


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['hello'])
def greeting(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

@bot.message_handler(commands=['help','start'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name} , для \
работы воспользуйтесь одним из методов\
b (пока работает только 1),\
введите валюты в формате <валюта на которую меняют> <валюта которую меняют> <количество>\
\в групповых чатах команда начинается с /\
\nвведите /values для списка доступных валют\
\nвведите /hello для приветствия' )

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for cur in currency.keys():
        text = str.title('\n'.join((text, cur, )))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convertion(message: telebot.types.Message):
    a = message.text.replace('/','')
    user_input = list(map(str.lower, a.split(' ')))


    bot.send_message(message.chat.id, Converter.get_price(user_input))



bot.polling(none_stop = True)
