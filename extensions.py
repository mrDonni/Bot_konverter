import json
import requests

from config import  currency

class Bot_exception(BaseException):
    pass


class Converter:
    @staticmethod
    def get_price(user_input):
        if len(user_input) !=3:
            raise Bot_exception
        quote, base, ammount = user_input

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={currency[base]}&symbols={currency[quote]}')
        data = json.loads(r.content)['rates'][currency[quote]]
        result = round(float(data) * float(ammount), 3)
        return f'{result} {quote} в {ammount} {base}'