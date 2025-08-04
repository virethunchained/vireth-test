# vireth_rle/plugins/emotion_utils.py

import re

def infer_emotion(text):
    lowered = text.lower()

    def has_any(patterns):
        return any(re.search(rf'\b{re.escape(word)}\b', lowered) for word in patterns)

    if has_any(["frustrated", "angry", "mad", "furious", "annoyed", "enraged", "outraged", "irritated"]):
        return "anger"
    elif has_any(["thrilled", "excited", "happy", "joyful", "ecstatic", "elated", "cheerful", "glad"]):
        return "joy"
    elif has_any(["sad", "disappointed", "upset", "miserable", "heartbroken", "down"]):
        return "sadness"
    elif has_any(["proud", "accomplished", "achievement", "success", "fulfilled"]):
        return "pride"
    elif has_any(["anxious", "worried", "nervous", "scared", "afraid", "uneasy"]):
        return "fear"
    else:
        return "neutral"
