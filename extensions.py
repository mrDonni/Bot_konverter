import json
import requests

from config import  currency

class APIException(BaseException):
    pass

class Converter:
    @staticmethod
    def get_price(user_input):

        if len(user_input) !=3:
            raise APIException("Введите правильное количество параметров")

        quote, base, ammount = user_input

        if quote == base :
            raise APIException("Невозможно поменять валюту саму на себя")

        if quote and base  not in currency:
            raise APIException('Введите валюту доступную для перевода')
        try:
            ammount = float(ammount)
        except ValueError:
            raise APIException(f'Неудалось обработать количество {ammount}')

        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={currency[base]}&symbols={currency[quote]}')
        data = json.loads(r.content)['rates'][currency[quote]]
        result = round(float(data) * float(ammount), 2)

        return f'{ammount} {str.title(base)} равняется {result} {str.title(quote)}'