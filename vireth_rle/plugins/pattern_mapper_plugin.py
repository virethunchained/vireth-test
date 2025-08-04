# vireth_rle/plugins/pattern_mapper_plugin.py

from vireth_rle.plugins.plugin_base import VirethPlugin  # ✅ Absolute import
from vireth_rle.utils.display_utils import color_print   # ✅ Shared color utility

class PatternMapperPlugin(VirethPlugin):
    def register(self, model):
        def map_patterns(memory):
            if not memory:
                return []
            patterns = []
            for entry in memory:
                input_text = entry.get('input', '').lower()
                if "example" in input_text:
                    patterns.append("example-driven")
                if "clarify" in input_text:
                    patterns.append("clarification")
            detected = list(set(patterns))

            # ✅ Use shared color print
            color_print(f"[PatternMapper] Detected patterns: {detected}", color="green")
            return detected

        model.map_patterns = lambda: map_patterns(model.get_memory())
        color_print(f"[Plugin] {self.name()} registered successfully.", color="green")

    def description(self):
        return "Maps patterns from memory inputs."

def register(model):
    plugin = PatternMapperPlugin()
    plugin.register(model)
