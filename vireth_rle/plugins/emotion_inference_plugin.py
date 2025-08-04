from vireth_rle.plugins.plugin_base import VirethPlugin

class EmotionInferencePlugin(VirethPlugin):
    def register(self, model):
        def infer_emotion(input_text):
            lowered = input_text.lower()
            if any(word in lowered for word in ["happy", "joy", "excited", "love"]):
                emotion = "joy"
            elif any(word in lowered for word in ["angry", "frustrated", "annoyed", "hate"]):
                emotion = "anger"
            elif any(word in lowered for word in ["sad", "upset", "depressed"]):
                emotion = "sadness"
            else:
                emotion = "neutral"

            # ✅ Store the last inferred emotion for insight logging
            model.last_inferred_emotion = emotion

            # ✅ Color-coded terminal output
            color_map = {
                "joy": "\033[93m",      # Yellow
                "anger": "\033[91m",    # Red
                "sadness": "\033[94m",  # Blue
                "neutral": "\033[90m",  # Gray
            }
            reset = "\033[0m"
            color = color_map.get(emotion, "\033[0m")

            print(f"{color}[EmotionInference] Detected emotion: {emotion}{reset}")
            return emotion

        # Attach the function to the model
        model.infer_emotion = infer_emotion
        print(f"[Plugin] {self.name()} registered successfully.")

    def description(self):
        return "Infers basic emotions from input text."

def register(model):
    plugin = EmotionInferencePlugin()
    plugin.register(model)
