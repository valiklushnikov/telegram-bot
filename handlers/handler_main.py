from handlers.handler_commands import HandlerCommands
from handlers.handler_query import HandlerQuery


class HandlerMain:
    def __init__(self, bot):
        self.bot = bot
        self.user_amount = None
        self.user_currency = None
        self.handler_commands = HandlerCommands(bot, self)
        self.handler_query = HandlerQuery(bot, self)

    def handle(self):
        self.handler_commands.handle()
        self.handler_query.handle()
