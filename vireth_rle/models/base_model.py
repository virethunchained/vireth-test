from vireth_rle.utils.memory_utils import MemoryBuffer
from vireth_rle.utils.feedback_utils import FeedbackLog
from vireth_rle.utils.recursive_utils import RecursiveReasoner, RecursiveChainTracker
from vireth_rle.utils.learning_utils import LearningHook
from vireth_rle.utils.insight_utils import InsightLog  # existing

class BaseModel:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.memory = MemoryBuffer()
        self.feedback = FeedbackLog()
        self.reasoner = RecursiveReasoner()
        self.chain_tracker = RecursiveChainTracker()
        self.learning = LearningHook()
        self.insight_log = InsightLog()
        self.preprocessors = []  # ✅ NEW

    def describe(self):
        print(f"Model Name: {self.name}")
        print(f"Version: {self.version}")

    def register_preprocessor(self, fn):  # ✅ NEW
        self.preprocessors.append(fn)

    def process_input(self, input_text):
        # ✅ Apply preprocessing hooks
        for fn in self.preprocessors:
            input_text = fn(input_text)

        # Core output
        output = f"Processed input: {input_text}"

        # Recursive logic tracking
        self.chain_tracker.analyze("Interpreting input")
        self.chain_tracker.reflect("Evaluating prior outputs")
        self.chain_tracker.iterate("Refining based on context")

        # Recursive refinement
        refined_output = self.reasoner.refine(output)

        # Store in memory
        self.memory.add(input_text, refined_output)

        # Observe for learning
        self.learning.observe(input_text, refined_output)

        # Log insight
        insight = f"From '{input_text}' ➝ '{refined_output}'"

        return refined_output

    def get_memory(self):
        return self.memory.get_recent()

    def add_feedback(self, note):
        self.feedback.add_feedback(note)

    def get_feedback(self):
        return self.feedback.get_all_feedback()

    def get_reasoning_chain(self):
        return self.chain_tracker.get_chain()

    def reset_reasoning_chain(self):
        self.chain_tracker.reset()

    def get_insights(self):
        return self.learning.get_insights()

    def get_logged_insights(self):  # ✅ NEW
        return self.insight_log.get_all()

