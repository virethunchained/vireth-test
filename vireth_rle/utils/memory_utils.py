# vireth_rle/utils/memory_utils.py

import json
import os

MEMORY_PATH = "memory.json"

class MemoryBuffer:
    def __init__(self):
        self.buffer = self._load_from_disk()

    def _load_from_disk(self):
        if os.path.exists(MEMORY_PATH):
            try:
                with open(MEMORY_PATH, "r") as f:
                    return json.load(f)
            except Exception as e:
                print(f"[MemoryBuffer] Failed to load from disk: {e}")
                return []
        return []

    def _save_to_disk(self):
        try:
            with open(MEMORY_PATH, "w") as f:
                json.dump(self.buffer, f, indent=2)
        except Exception as e:
            print(f"[MemoryBuffer] Failed to save to disk: {e}")

    def add(self, input_text, output_text):
        entry = {
            "input": input_text,
            "output": output_text
        }
        self.buffer.append(entry)
        self._save_to_disk()

    def get_recent(self, n=10):
        return self.buffer[-n:]
