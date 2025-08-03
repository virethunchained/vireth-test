# vireth_rle/plugins/emotion_inference_plugin.py

from vireth_rle.plugins import plugin_base
from vireth_rle.plugins.emotion_utils import infer_emotion

def register(model):
    def emotion_hook(text):
        emotion = infer_emotion(text)
        print(f"[EmotionInference] Detected emotion: {emotion}")
        return text  # No modification for now; could adapt if needed

    model.register_preprocessor(emotion_hook)
    print("[Plugin] EmotionInferencePlugin registered successfully.")
