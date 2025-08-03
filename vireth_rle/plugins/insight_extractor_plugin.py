from vireth_rle.plugins.plugin_base import VirethPlugin

class InsightExtractorPlugin(VirethPlugin):
    def register(self, model):
        def extract_insights():
            return [entry['output'] for entry in model.get_memory() if "Refined" in entry['output']]

        model.extract_insights = extract_insights
        print(f"[Plugin] {self.name()} registered successfully.")

    def description(self):
        return "Extracts key insights from memory."

def register(model):
    plugin = InsightExtractorPlugin()
    plugin.register(model)
