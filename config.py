import telebot


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
    for key in currency.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convertion(message: telebot.types.Message):

currency = {
    'Доллар': 'USD',
    'Рубль': 'RUB',
    'Евро': 'EUR'
}


bot.polling(none_stop = True)