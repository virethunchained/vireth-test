# vireth_rle/plugins/plugin_base.py

class VirethPlugin:
    """
    Base interface for all Vireth plugins.
    Each plugin must implement a register(model) method.
    Optional lifecycle hooks can also be defined.
    """

    def register(self, model):
        """
        Mandatory method to register plugin capabilities with the model.
        """
        raise NotImplementedError("Plugin must implement register(model)")

    def name(self):
        """
        Optional: return the name of the plugin
        """
        return self.__class__.__name__

    def description(self):
        """
        Optional: return a brief description of what the plugin does
        """
        return "No description provided."
