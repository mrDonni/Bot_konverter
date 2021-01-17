import telebot
import json
import requests

currency = {
    'доллар': 'USD',
    'рубль': 'RUB',
    'евро': 'EUR'
}
r = requests.get(f'https://api.exchangeratesapi.io/latest?base=USD&symbols=RUB')
data = json.loads(r.content)

print(r.content)
print(data)
print(data['rates']['RUB'])