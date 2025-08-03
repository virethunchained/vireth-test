from vireth_rle.utils.memory_utils import MemoryBuffer
from vireth_rle.utils.feedback_utils import FeedbackLog

class BaseModel:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.memory = MemoryBuffer()
        self.feedback = FeedbackLog()

    def describe(self):
        print(f"Model Name: {self.name}")
        print(f"Version: {self.version}")

    def process_input(self, input_text):
        output = f"Processed input: {input_text}"
        self.memory.add(input_text, output)
        return output

    def get_memory(self):
        return self.memory.get_recent()

    def add_feedback(self, note):
        self.feedback.add(note)

    def get_feedback(self):
        return self.feedback.show()
