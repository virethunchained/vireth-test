from vireth_rle.plugins.plugin_base import VirethPlugin
from vireth_rle.utils.insight_utils import log_insight

class InsightExtractorPlugin(VirethPlugin):
    def register(self, model):
        def extract_insights():
            insights = [
                entry['output']
                for entry in model.get_memory()
                if "Refined" in entry['output']
            ]
            for insight in insights:
                log_insight(model, insight)
            return insights

        model.extract_insights = extract_insights
        print(f"[Plugin] {self.name()} registered successfully.")

    def description(self):
        return "Extracts key insights from memory and logs them."

def register(model):
    plugin = InsightExtractorPlugin()
    plugin.register(model)
