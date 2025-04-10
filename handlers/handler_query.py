from handlers.handler import Handler
from settings.currency_codes import currency_codes
from datetime import datetime
from settings import config


class HandlerQuery(Handler):
    def __init__(self, bot, main_handler):
        super().__init__(bot)
        self.main_handler = main_handler

    def get_currency(self, currency):
        iso_code = currency_codes.get(currency, {}).get("ISOnum")
        currency_obj = next(
            currency
            for currency in self.currency.data
            if int(currency.get("currencyCodeA") == int(iso_code))
        )
        return currency_obj if currency_obj else {}

    def get_transaction(self, amount, currency, exchanged_amount, date):
        return {
            "amount": amount,
            "currency": currency,
            "exchange_amount": exchanged_amount,
            "date": datetime.fromtimestamp(date).strftime("%d-%B-%Y %H:%M:%S"),
        }

    def get_user(self, data):
        return {
            "telegram_id": data.chat.id,
            "first_name": data.chat.first_name,
            "last_name": data.chat.last_name if data.chat.last_name else "",
        }

    def handle(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def handle(call):
            if call.data == "BACK":
                self.main_handler.handler_commands.pressed_btn_start(call.message)
                return
            if call.data == "INFO":
                self.main_handler.handler_commands.pressed_btn_info(call.message)
                return
            if call.data == "CONVERT":
                self.main_handler.handler_commands.pressed_btn_convert(call.message)
                return
            if call.data == "START":
                self.main_handler.handler_commands.pressed_btn_start(call.message)
                return
            if call.data == "OTHER":
                self.main_handler.handler_commands.pressed_btn_other_currency(call.message)
                return

            currency = self.main_handler.user_currency if call.data == "ELSE" else call.data
            currency_obj = self.get_currency(currency)
            amount = self.main_handler.user_amount

            if "rateSell" in currency_obj:
                exchanged_amount = round(amount / float(currency_obj["rateSell"]), 2)
            else:
                exchanged_amount = round(amount / float(currency_obj["rateCross"]), 2)

            transaction = self.get_transaction(
                amount, currency, exchanged_amount, call.message.date
            )
            user = self.get_user(call.message)

            self.DB._add_transaction(user, transaction)

            self.file_saver.add_to_json(call.message.chat.id, transaction)

            self.bot.send_message(
                call.message.chat.id,
                config.CONTENT["AMOUNT_MSG"].format(currency, exchanged_amount),
                parse_mode="HTML",
                reply_markup=self.keyboards.info_menu(),
            )
