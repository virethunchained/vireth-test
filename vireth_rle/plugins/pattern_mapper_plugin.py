# vireth_rle/plugins/pattern_mapper_plugin.py

from vireth_rle.plugins.plugin_base import VirethPlugin  # ✅ Absolute import

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

            # ✅ Color-coded output
            color = "\033[92m"  # Light green
            reset = "\033[0m"
            print(f"{color}[PatternMapper] Detected patterns: {detected}{reset}")

            return detected

        model.map_patterns = lambda: map_patterns(model.get_memory())
        print(f"[Plugin] {self.name()} registered successfully.")

    def description(self):
        return "Maps patterns from memory inputs."

def register(model):
    plugin = PatternMapperPlugin()
    plugin.register(model)
