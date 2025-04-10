import requests
from common.interface import Singleton


class CurrencyAPI(metaclass=Singleton):
    BASE_URL = "https://api.monobank.ua/bank/currency"

    def __init__(self):
        self._data = None

    def _get_data(self):
        try:
            response = requests.get(self.BASE_URL)
            return response.json()
        except requests.RequestException as e:
            print(e)
        return {}

    @property
    def data(self):
        if self._data is None:
            self._data = self._get_data()
        return self._data
