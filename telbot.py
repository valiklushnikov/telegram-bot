from time import sleep
from telebot import TeleBot
from telebot.types import Update

from flask import Flask, request, Response

from settings import config
from handlers.handler_main import HandlerMain
import set_webhook


app = Flask(__name__)


class TelBot:

    __version__ = config.VERSION
    __author__ = config.AUTHOR

    def __init__(self):
        self.token = config.TOKEN
        self.bot = TeleBot(self.token, threaded=True, num_threads=4, skip_pending=True)
        self.handler = HandlerMain(self.bot)

    def start(self):
        self.handler.handle()
        self.bot.remove_webhook()
        sleep(1)
        # self.bot.set_webhook(
        #     url=config.SERV_URL,
        #     allowed_updates=["message", "callback_query"],
        # )

telbot = TelBot()
telbot.start()


@app.route("/", methods=["POST"])
def webhook():
    if request.headers.get("content-type") == "application/json":
        json_string = request.get_data().decode("utf-8")
        update = Update.de_json(json_string)
        telbot.bot.process_new_updates([update])
        return Response("OK", status=200)
    return Response("Unsupported Media Type", status=415)


if __name__ == "__main__":
    set_webhook.set_webhook()
    app.run(host="0.0.0.0", port=5000)
