import os
import json
from datetime import datetime

INSIGHT_MEMORY_FILE = "insights.json"

def load_insights_from_disk():
    if not os.path.exists(INSIGHT_MEMORY_FILE):
        return []
    try:
        with open(INSIGHT_MEMORY_FILE, "r") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except Exception as e:
        print(f"[PersistentMemory] Failed to load insights: {e}")
        return []

def append_insight_to_disk(insight):
    try:
        insights = load_insights_from_disk()
        insights.append(insight)
        with open(INSIGHT_MEMORY_FILE, "w") as f:
            json.dump(insights, f, indent=2)
    except Exception as e:
        print(f"[PersistentMemory] Failed to save insight: {e}")
