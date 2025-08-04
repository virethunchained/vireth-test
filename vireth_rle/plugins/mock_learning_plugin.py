from vireth_rle.plugins.plugin_base import VirethPlugin

class MockLearningPlugin(VirethPlugin):
    def register(self, model):
        def show_mock_growth():
            print("\n[Mock Plugin] Simulated Growth Insight:")
            print("Vireth is capable of reflecting on symbolic logic and recursion.")

        model.show_mock_growth = show_mock_growth
        print(f"[Plugin] {self.name()} registered successfully.")

    def description(self):
        return "Demonstrates mock learning feedback."

def register(model):
    plugin = MockLearningPlugin()
    plugin.register(model)
