class PluginInterface:
    @staticmethod
    def execute(var: list):
        raise NotImplementedError()
    
    @staticmethod
    def draw(layout):
        raise NotImplementedError()