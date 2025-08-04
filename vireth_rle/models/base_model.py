from vireth_rle.utils.memory_utils import MemoryBuffer
from vireth_rle.utils.feedback_utils import FeedbackLog
from vireth_rle.utils.recursive_utils import RecursiveReasoner, RecursiveChainTracker
from vireth_rle.utils.learning_utils import LearningHook
from vireth_rle.utils.insight_utils import InsightLog, log_insight  # ✅ Updated import

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
        self.preprocessors = []
        self.learned_insights = []
        self.last_tagged_topic = None  # ✅ Stores last topic
        self.last_inferred_emotion = None  # ✅ Stores last inferred emotion
        self.last_detected_patterns = []   # ✅ Stores last detected patterns

    def describe(self):
        print(f"Model Name: {self.name}")
        print(f"Version: {self.version}")

    def register_preprocessor(self, fn):
        self.preprocessors.append(fn)

    def process_input(self, input_text):
        # ✅ Apply preprocessing hooks
        for fn in self.preprocessors:
            input_text = fn(input_text)

        # Core output generation
        output = f"Processed input: {input_text}"

        # Recursive logic tracking
        self.chain_tracker.analyze("Interpreting input")
        self.chain_tracker.reflect("Evaluating prior outputs")
        self.chain_tracker.iterate("Refining based on context")

        # Recursive refinement
        refined_output = self.reasoner.refine(output)

        # ✅ Tag topic if available
        if hasattr(self, "tag_topic"):
            self.last_tagged_topic = self.tag_topic(input_text)

        # ✅ Infer emotion if available
        if hasattr(self, "infer_emotion"):
            self.last_inferred_emotion = self.infer_emotion(input_text)

        # ✅ Map patterns if available
        if hasattr(self, "map_patterns"):
            self.last_detected_patterns = self.map_patterns()

        # Store in memory
        self.memory.add(input_text, refined_output)

        # Observe for learning
        self.learning.observe(input_text, refined_output)

        # ✅ Log structured insight
        log_insight(
            self,
            refined_output,
            topic=self.last_tagged_topic,
            emotion=self.last_inferred_emotion,
            patterns=self.last_detected_patterns,
            reasoning=self.get_reasoning_chain()
        )

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

    def get_logged_insights(self):
        return self.insight_log.get_all()
