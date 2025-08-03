from vireth_rle.plugins.plugin_base import VirethPlugin

class TopicTaggerPlugin(VirethPlugin):
    def register(self, model):
        def tag_topic(text):
            if "logic" in text.lower():
                return "Logic"
            elif "recursion" in text.lower():
                return "Recursion"
            else:
                return "General"

        model.tag_topic = tag_topic
        print(f"[Plugin] {self.name()} registered successfully.")

    def description(self):
        return "Tags dominant topic in input."

def register(model):
    plugin = TopicTaggerPlugin()
    plugin.register(model)
