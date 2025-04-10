from handlers.handler import Handler
from settings.currency_codes import currency_codes
from settings import config


class HandlerCommands(Handler):
    def __init__(self, bot, main_handler):
        super().__init__(bot)
        self.main_handler = main_handler

    def pressed_btn_start(self, message):
        self.bot.send_message(
            message.chat.id,
            config.CONTENT["GREETING_MENU"],
            parse_mode="HTML",
            reply_markup=self.keyboards.start_menu(),
        )

    def pressed_btn_convert(self, message):
        self.bot.send_message(
            message.chat.id,
            config.CONTENT["CONVERT_MENU"],
            parse_mode="HTML",
        )
        self.bot.register_next_step_handler(message, self.set_user_amount)

    def pressed_btn_other_currency(self, message):
        self.bot.send_message(
            message.chat.id,
            config.CONTENT["OTHER_CURRENCY"],
            parse_mode="HTML",
        )
        self.bot.register_next_step_handler(message, self.set_user_currency)

    def pressed_btn_info(self, message):
        ts = [t.to_dict() for t in self.DB._get_all_transaction(message.chat.id)]

        message_text = "\n\n".join(
            f"💸 Amount: {t['amount']}\n"
            f"💱 Currency: {t['currency']}\n"
            f"🔄 Converted: {t['exchange_amount']}\n"
            f"🕒 Date: {t['date']}"
            for t in ts[::-1]
        )

        self.bot.send_message(
            message.chat.id,
            f"📜 Your transactions:\n\n{message_text}",
            reply_markup=self.keyboards.history_menu(),
        )

    def set_user_amount(self, message):
        amount = message.text.strip().split()

        if len(amount) > 1:
            self.bot.send_message(message.chat.id, config.CONTENT["INVALID_CURRENCY"])
            self.bot.register_next_step_handler(message, self.set_user_amount)
            return
        try:
            self.main_handler.user_amount = float(amount[0])
        except ValueError:
            self.bot.send_message(message.chat.id, config.CONTENT["INVALID_FORMAT"])
            self.bot.register_next_step_handler(message, self.set_user_amount)
            return
        if self.main_handler.user_amount > 0:
            self.bot.send_message(
                message.chat.id,
                config.CONTENT["USER_AMOUNT_MSG"].format(self.main_handler.user_amount),
                parse_mode="HTML",
                reply_markup=self.keyboards.user_menu(),
            )
        else:
            self.bot.send_message(message.chat.id, config.CONTENT["AMOUNT_ZERO"])
            self.bot.register_next_step_handler(message, self.set_user_amount)

    def set_user_currency(self, message):
        user_currencies = message.text.strip().split()
        if len(user_currencies) != 1:
            self.bot.send_message(message.chat.id, config.CONTENT["INVALID_CURRENCY"])
            self.bot.register_next_step_handler(message, self.set_user_currency)
            return
        else:
            to_currency = user_currencies[0].upper()
            if to_currency not in currency_codes:
                self.bot.send_message(
                    message.chat.id, config.CONTENT["INVALID_CURRENCY"]
                )
                self.bot.register_next_step_handler(message, self.set_user_currency)
                return
            else:
                self.main_handler.user_currency = to_currency
                self.bot.send_message(
                    message.chat.id,
                    config.CONTENT["USER_CURRENCY_MSG"].format(
                        self.main_handler.user_amount,
                        to_currency,
                    ),
                    parse_mode="HTML",
                    reply_markup=self.keyboards.confirm_menu(),
                )

    def handle(self):
        @self.bot.message_handler(commands=["start"])
        def handle(message):
            if message.text == "/start":
                self.pressed_btn_start(message)
