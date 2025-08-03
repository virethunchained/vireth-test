# vireth_rle/utils/insight_utils.py

class InsightLog:
    def __init__(self):
        self.entries = []

    def log(self, insight: str):
        if insight and isinstance(insight, str):
            self.entries.append(insight)
            print(f"[InsightLog] Logged insight: {insight}")

    def get_all(self):
        return self.entries

