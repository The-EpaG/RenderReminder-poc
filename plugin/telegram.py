from lib import PluginInterface


class TelegramPlugin(PluginInterface):
    token: str = "token"
    chatId: str = "chatId"

    @staticmethod
    def execute(vars: list):
        print(f"{TelegramPlugin.__name__}: {vars}")
    
    @staticmethod
    def draw(layout):
        layout.append(f"{TelegramPlugin.__name__}.token")
        layout.append(f"{TelegramPlugin.__name__}.chatId")