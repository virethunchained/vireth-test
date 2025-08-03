from vireth_rle.utils.memory_utils import MemoryBuffer
from vireth_rle.utils.feedback_utils import FeedbackLog
from vireth_rle.utils.recursive_utils import RecursiveReasoner

class BaseModel:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.memory = MemoryBuffer()
        self.feedback = FeedbackLog()
        self.reasoner = RecursiveReasoner()

    def describe(self):
        print(f"Model Name: {self.name}")
        print(f"Version: {self.version}")

    def process_input(self, input_text):
        # Core output
        output = f"Processed input: {input_text}"

        # Optional recursive refinement
        refined_output = self.reasoner.refine(output)
        self.memory.add(input_text, refined_output)
        return refined_output

    def get_memory(self):
        return self.memory.get_recent()

    def add_feedback(self, note):
        self.feedback.add_feedback(note)

    def get_feedback(self):
        return self.feedback.get_all_feedback()
