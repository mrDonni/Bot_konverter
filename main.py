import telebot
from config import TOKEN, currency
from extensions import Converter , APIException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['hello'])
def greeting(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')

@bot.message_handler(commands=['help', 'start'])
def help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name} , для \
работы воспользуйтесь одним из методов\
 (пока работает только 1)\
\n1)введите валюты в формате <валюта на которую меняют>\
 <валюта которую меняют> <количество> через пробел\
\nВ групповых чатах команда начинается со знака /\
\nВведите /values для списка доступных валют\
\nВведите /hello для приветствия\
\nВведите /start, /help для помощи')

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for cur in currency.keys():
        text = str.title('\n'.join((text, cur, )))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convertion(message: telebot.types.Message):
    try:
        a = message.text.replace('/','')
        user_input = list(map(str.lower, a.split(' ')))

        bot.send_message(message.chat.id, Converter.get_price(user_input))

    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')

    except Exception as e:
        bot.reply_to(message,f' не удалось обработать команду\n{e}')


bot.polling(none_stop = True)
