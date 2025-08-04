from datetime import datetime
from vireth_rle.utils.persistent_memory import load_insights_from_disk, append_insight_to_disk

class InsightLog:
    def __init__(self):
        # ✅ Load persistent insights at startup
        self.entries = load_insights_from_disk()

    def add(self, structured_insight):
        """
        Adds a structured insight entry with timestamp, topic, emotion, patterns, reasoning, etc.
        Also persists it to disk.
        """
        self.entries.append(structured_insight)
        append_insight_to_disk(structured_insight)
        print(f"[InsightLog] Logged structured insight: {structured_insight['text']}")

    def get_all(self):
        return self.entries

def log_insight(model, text, topic=None, emotion=None, patterns=None, reasoning=None, timestamp=None):
    """
    Logs a structured insight into the model's InsightLog and appends to model.learned_insights.
    """
    structured_entry = {
        "text": text,
        "topic": topic or getattr(model, 'last_tagged_topic', None),
        "emotion": emotion or getattr(model, 'last_inferred_emotion', None),
        "patterns": patterns or getattr(model, 'last_detected_patterns', []),
        "reasoning": reasoning or model.get_reasoning_chain(),
        "timestamp": timestamp or datetime.utcnow().isoformat()
    }

    model.insight_log.add(structured_entry)
    model.learned_insights.append(structured_entry)

