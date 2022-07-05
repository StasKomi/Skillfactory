import requests
import json
from config import keys, APIKEY


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')
        r = requests.get(f'https://currate.ru/api/?get=rates&pairs={quote_ticker + base_ticker}&key={APIKEY}')
        total_base = json.loads(r.content)['data'][f'{quote_ticker + base_ticker}']
        return total_base

    @staticmethod
    def useless_fact(amount: str):
        f = requests.get(f'http://numbersapi.com/{amount}').text
        return f
