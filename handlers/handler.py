import abc
from markup.markup import Keyboards
from data_base.dbalchemy import DBManager
from services.services import CurrencyAPI
from services.file_saver import JSONSaver


class Handler(metaclass=abc.ABCMeta):
    def __init__(self, bot):
        self.bot = bot
        self.keyboards = Keyboards()
        self.file_saver = JSONSaver()
        self.currency = CurrencyAPI()
        self.DB = DBManager()

    @abc.abstractmethod
    def handle(self):
        pass
