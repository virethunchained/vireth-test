from datetime import datetime
from vireth_rle.utils.persistent_memory import load_insights_from_disk, append_insight_to_disk
from vireth_rle.utils.display_utils import color_print  # ✅ Color utility

class InsightLog:
    def __init__(self):
        """
        Initializes the InsightLog by loading existing persistent insights from disk.
        """
        self.entries = load_insights_from_disk()

    def add(self, structured_insight):
        """
        Adds a structured insight entry with timestamp, topic, emotion, patterns, reasoning, etc.
        Also persists it to disk.
        """
        self.entries.append(structured_insight)
        append_insight_to_disk(structured_insight)

        # ✅ Color-coded log output
        color_print(
            f"[InsightLog] Logged structured insight: {structured_insight['text']}",
            tag="log",
            subtype="insight"
        )

    def get_all(self):
        """
        Returns all logged insights.
        """
        return self.entries

def log_insight(model, text, topic=None, emotion=None, patterns=None, reasoning=None, timestamp=None):
    """
    Logs a structured insight into the model's InsightLog and appends to model.learned_insights.

    Args:
        model: The active BaseModel instance.
        text (str): The insight text.
        topic (str): Tagged topic (optional).
        emotion (str): Inferred emotion (optional).
        patterns (list): Recognized patterns (optional).
        reasoning (list): Reasoning chain (optional).
        timestamp (str): Timestamp override (optional).
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
