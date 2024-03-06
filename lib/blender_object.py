from lib.plugin_interface import PluginInterface
from lib import Injectable, extract_vars


class BlenderObject(Injectable):
    def __init__(self, plugins: list[type[PluginInterface]]):
        self.plugins: list[type] = plugins
        self.layout: list[str] = []

        self._auto_inject()

    def _auto_inject(self):
        for plugin in self.plugins:
            vars = extract_vars(plugin)
            for name, value in vars.items():
                self.inject(f"{plugin.__name__}.{name}", value)
            print(f"{plugin.__name__} injected")
    
    def draw(self):
        for plugin in self.plugins:
            if not issubclass(plugin, PluginInterface):
                continue

            plugin.draw(self.layout)

    def _filter_vars(self, plugin:str):
        vars = dict(
                filter(
                    lambda var: var[0].startswith(plugin),
                    extract_vars(self).items(),
                )
            )
        return dict(
                map(lambda var: (var[0].replace(f"{plugin}.", ""), var[1]), vars.items())
            )
        
    def execute(self):
        for plugin in self.plugins:
            if not issubclass(plugin, PluginInterface):
                continue

            plugin.execute(self._filter_vars(plugin.__name__))
