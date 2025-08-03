# vireth_rle/plugins/logic_transformer_plugin.py

from vireth_rle.plugins.plugin_base import VirethPlugin  # ✅ Absolute import

class LogicTransformerPlugin(VirethPlugin):
    def register(self, model):
        def transform_logic(statement):
            # Very simple symbolic logic normalization (mock for now)
            normalized = statement.replace("and", "∧").replace("or", "∨").replace("not", "¬")
            print(f"[LogicTransformer] Transformed: '{statement}' ➝ '{normalized}'")
            return normalized

        # Attach the function to the model
        model.transform_logic = transform_logic
        print(f"[Plugin] {self.name()} registered successfully.")

    def description(self):
        return "Transforms logical statements into canonical symbolic forms."

# Required for plugin loader
def register(model):
    plugin = LogicTransformerPlugin()
    plugin.register(model)
