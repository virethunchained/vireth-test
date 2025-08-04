# vireth_rle/plugins/topic_tagger_plugin.py

from vireth_rle.plugins.plugin_base import VirethPlugin

class TopicTaggerPlugin(VirethPlugin):
    def register(self, model):
        def tag_topic(text):
            lowered = text.lower()
            if "logic" in lowered:
                topic = "Logic"
            elif "recursion" in lowered:
                topic = "Recursion"
            else:
                topic = "General"
            model.last_tagged_topic = topic  # ✅ Store for later access

            # ✅ Color-coded topic output
            color_map = {
                "Logic": "\033[95m",      # Magenta
                "Recursion": "\033[96m",  # Cyan
                "General": "\033[90m",    # Gray
            }
            reset = "\033[0m"
            color = color_map.get(topic, "\033[0m")

            print(f"{color}[TopicTagger] Tagged topic: {topic}{reset}")
            return topic

        model.tag_topic = tag_topic
        print(f"[Plugin] {self.name()} registered successfully.")

    def description(self):
        return "Tags dominant topic in input."

def register(model):
    plugin = TopicTaggerPlugin()
    plugin.register(model)
