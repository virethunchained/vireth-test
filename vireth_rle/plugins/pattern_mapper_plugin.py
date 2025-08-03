from vireth_rle.plugins.plugin_base import VirethPlugin  # ✅ Absolute import

class PatternMapperPlugin(VirethPlugin):
    def register(self, model):
        def map_patterns(memory):
            patterns = []
            for entry in memory:
                if "example" in entry['input'].lower():
                    patterns.append("example-driven")
                if "clarify" in entry['input'].lower():
                    patterns.append("clarification")
            return list(set(patterns))

        model.map_patterns = lambda: map_patterns(model.get_memory())
        print(f"[Plugin] {self.name()} registered successfully.")

    def description(self):
        return "Maps patterns from memory inputs."

def register(model):
    plugin = PatternMapperPlugin()
    plugin.register(model)
