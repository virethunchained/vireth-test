# vireth_rle/utils/feedback_utils.py

import json
import os

FEEDBACK_PATH = "feedback.json"

class FeedbackLog:
    def __init__(self):
        self.log = self._load_from_disk()

    def _load_from_disk(self):
        if os.path.exists(FEEDBACK_PATH):
            try:
                with open(FEEDBACK_PATH, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[FeedbackLog] Failed to load from disk: {e}")
                return []
        return []

    def _save_to_disk(self):
        try:
            with open(FEEDBACK_PATH, "w") as f:
                json.dump(self.log, f, indent=2)
        except Exception as e:
            print(f"[FeedbackLog] Failed to save to disk: {e}")

    def add_feedback(self, feedback):
        print(f"[FeedbackLog] Logging feedback: {feedback}")
        self.log.append(feedback)
        self._save_to_disk()

    def get_all_feedback(self):
        return self.log
