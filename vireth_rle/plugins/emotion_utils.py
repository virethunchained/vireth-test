# vireth_rle/plugins/emotion_utils.py

def infer_emotion(text):
    if any(word in text.lower() for word in ["happy", "joy", "glad", "love"]):
        return "positive"
    elif any(word in text.lower() for word in ["angry", "sad", "hate", "upset"]):
        return "negative"
    else:
        return "neutral"
