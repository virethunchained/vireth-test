from datetime import datetime

class InsightLog:
    def __init__(self):
        self.entries = []

    def add(self, structured_insight):
        """
        Adds a structured insight entry with timestamp, topic, emotion, patterns, reasoning, etc.
        """
        self.entries.append(structured_insight)
        print(f"[InsightLog] Logged structured insight: {structured_insight['text']}")

    def get_all(self):
        return self.entries

def log_insight(model, text, topic=None, emotion=None, patterns=None, reasoning=None):
    """
    Logs a structured insight into the model's InsightLog and appends to model.learned_insights.
    """
    structured_entry = {
        "text": text,
        "topic": topic or getattr(model, 'last_tagged_topic', None),
        "emotion": emotion or getattr(model, 'last_inferred_emotion', None),
        "patterns": patterns or getattr(model, 'last_detected_patterns', []),
        "reasoning": reasoning or model.get_reasoning_chain(),
        "timestamp": datetime.utcnow().isoformat()
    }

    model.insight_log.add(structured_entry)
    model.learned_insights.append(structured_entry)
