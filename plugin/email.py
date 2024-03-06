from lib import PluginInterface

class EmailPlugin(PluginInterface):
    imap_server:str = "localhost"
    imap_port:int = 1234
    email_from:str = "email@email.it"
    email_to:str = "email@email.it"
    password:str = "supersecret"

    @staticmethod
    def execute(vars:list):
        print(f"{EmailPlugin.__name__}: {vars}")
    
    @property
    @staticmethod
    def text():
        return "hi"

    @staticmethod
    def draw(layout):
        layout.append(f"{EmailPlugin.__name__}.imap_server")
        layout.append(f"{EmailPlugin.__name__}.imap_port")
        layout.append(f"{EmailPlugin.__name__}.email_from")
        layout.append(f"{EmailPlugin.__name__}.email_to")
        layout.append(f"{EmailPlugin.__name__}.password")
        layout.append(f"{EmailPlugin.__name__}.text")