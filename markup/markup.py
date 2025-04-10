from telebot.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from settings import config
from data_base.dbalchemy import DBManager


class Keyboards:
    def __init__(self):
        self.markup = None
        self.DB = DBManager()

    def set_inline_btn(self, name, callback_data=None):
        return InlineKeyboardButton(config.KEYBOARD[name], callback_data=callback_data)

    def start_menu(self):
        self.markup = InlineKeyboardMarkup(row_width=1)
        btn_1 = self.set_inline_btn("EXCHANGE", callback_data="CONVERT")
        self.markup.add(btn_1)
        return self.markup

    def user_menu(self):
        self.markup = InlineKeyboardMarkup(row_width=3)
        btn_1 = self.set_inline_btn("USD", callback_data="USD")
        btn_2 = self.set_inline_btn("EUR", callback_data="EUR")
        btn_3 = self.set_inline_btn("GBP", callback_data="GBP")
        btn_4 = self.set_inline_btn("USER_CURRENCY", callback_data="OTHER")
        self.markup.add(btn_1, btn_2, btn_3, btn_4)
        return self.markup

    def info_menu(self):
        self.markup = InlineKeyboardMarkup(row_width=2)
        btn_1 = self.set_inline_btn("BACK", callback_data="CONVERT")
        btn_2 = self.set_inline_btn("INFO", callback_data="INFO")
        self.markup.add(btn_1, btn_2)
        return self.markup

    def confirm_menu(self, ):
        self.markup = InlineKeyboardMarkup(row_width=1)
        btn_1 = self.set_inline_btn("EXCHANGE", callback_data="ELSE")
        self.markup.add(btn_1)
        return self.markup

    def history_menu(self):
        self.markup = InlineKeyboardMarkup(row_width=1)
        btn_1 = self.set_inline_btn("BACK", callback_data="START")
        self.markup.add(btn_1)
        return self.markup
