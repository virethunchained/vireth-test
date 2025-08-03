class MemoryBuffer:
    def __init__(self):
        self.buffer = []

    def add(self, input_text, output_text):
        self.buffer.append({
            "input": input_text,
            "output": output_text
        })

    def get_recent(self, n=5):
        return self.buffer[-n:]

    def clear(self):
        self.buffer = []
