import telebot
import json
import requests



TOKEN ='1411716058:AAGHLhlcxHb_9J1mCRyxZHGossI1hO00GWA'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['hello'])
def greeting(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

@bot.message_handler(commands=['help','start'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name} , для \
работы воспользуйтесь одним из методов , введите /values для списка доступных валют' )

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for cur in currency.keys():
        text = '\n'.join((text, cur, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convertion(message: telebot.types.Message):
    user_input = list(map(str.lower, message.text.split(' ')))

    r = requests.get(f'https://api.exchangeratesapi.io/latest?base={currency[base]}&symbols={currency[quote]}')
    data = json.loads(r.content)['rates'][currency[quote]]
    result =round(float(data) * float(ammount), 3)
    bot.send_message(message.chat.id, result)



currency = {
    'доллар': 'USD',
    'рубль': 'RUB',
    'евро': 'EUR'
}


bot.polling(none_stop = True)