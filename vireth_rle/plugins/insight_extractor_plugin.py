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
                print(f"\033[96m[InsightExtractor] Logged refined insight: {insight}\033[0m")
            return insights

        model.extract_insights = extract_insights
        print(f"\033[96m[Plugin] {self.name()} registered successfully.\033[0m")

    def description(self):
        return "Extracts key insights from memory and logs them."

def register(model):
    plugin = InsightExtractorPlugin()
    plugin.register(model)
