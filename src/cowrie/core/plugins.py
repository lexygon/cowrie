class PluginManager:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super(PluginManager, cls).__new__(cls, *args, **kwargs)
        return cls.__instance

    plugins = []

    def instantiate_plugins(self, plugins, **instructions):
        instructions['plugin_manager'] = self
        for plugin in plugins:
            self.plugins.append(plugin(**instructions))

    def process_event(self, event, has_failed=False):
        for plugin in self.plugins:
            plugin.process_event(event, has_failed=has_failed)


class BasePlugin:
    def __init__(self, *args, **kwargs):
        self.plugin_manager = kwargs.get('plugin_manager')
        self.logger = kwargs.get('logger')

    def process_event(self, event, *args, **kwargs):
        raise NotImplementedError
