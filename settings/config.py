import os
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TOKEN")
SERV_URL = "https://4c91fbf3f1202bd1f3bb2b44adcd4508.serveo.net"

NAME_DB = "users.db"
VERSION = "1.0"
AUTHOR = "DanIT"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join("sqlite:///" + BASE_DIR, NAME_DB)

KEYBOARD = {
    "USD": "UAH/USD",
    "EUR": "UAH/EUR",
    "GBP": "UAH/GBP",
    "EXCHANGE": "🔄 Exchange",
    "USER_CURRENCY": "Select another",
    "INFO": "History",
    "BACK": "Back",
}
GREETING_MSG = """
Hello! I am a <b>MoneyExchanger</b> bot
I will help you make an exchange UAH. 💸
Select the desired item below: ⬇
"""
INVALID_CURRENCY = """
Invalid format currency amount!
Input correct format.
"""
INVALID_FORMAT = """
Invalid format amount!
Input correct format.
"""
AMOUNT_ZERO = """
Amount must be greater than 0.
Input correct amount.
"""
CONVERT_MSG = """
Input your amount to convert ⬇
Example format: <b><i>567</i></b>
"""
OTHER_CURRENCY_MSG = """
Input your currency to convert ⬇
Example format: THB, JPY, PLN
"""
AMOUNT_MSG = """
Your amount in <b>{}</b> is <b>{}</b>
"""
USER_AMOUNT_MSG = """
Your amount is <b><i>{}</i></b>.
Choose currency to convert.
"""
USER_CURRENCY_MSG = """
Your amount is <b><i>{}</i></b> convert to <b><i>{}</i></b>.
Select exchange to convert.
"""

CONTENT = {
    "GREETING_MENU": GREETING_MSG,
    "CONVERT_MENU": CONVERT_MSG,
    "INVALID_CURRENCY": INVALID_CURRENCY,
    "INVALID_FORMAT": INVALID_FORMAT,
    "AMOUNT_ZERO": AMOUNT_ZERO,
    "AMOUNT_MSG": AMOUNT_MSG,
    "USER_AMOUNT_MSG": USER_AMOUNT_MSG,
    "OTHER_CURRENCY": OTHER_CURRENCY_MSG,
    "USER_CURRENCY_MSG": USER_CURRENCY_MSG,
}

FILE_NAME = "user_data.json"
