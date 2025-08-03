# vireth_rle/utils/recursive_utils.py

class RecursiveProcessor:
    def __init__(self):
        self.steps = []

    def analyze(self, input_text):
        decision = f"Analyze: {input_text}"
        self.steps.append(decision)
        print(decision)
        return decision

    def reflect(self, previous_output):
        reflection = f"Reflect on: {previous_output}"
        self.steps.append(reflection)
        print(reflection)
        return reflection

    def iterate(self, new_input):
        return self.analyze(new_input)

    def summary(self):
        return self.steps


class RecursiveReasoner:
    def __init__(self):
        self.depth = 1  # Starting recursive depth

    def refine(self, text):
        # Simulate recursive refinement
        for i in range(self.depth):
            text = f"[Refined] {text}"
        return text


class RecursiveChainTracker:
    def __init__(self):
        self.chain = []

    def log_step(self, step_type, detail):
        entry = {"step": step_type, "detail": detail}
        self.chain.append(entry)
        print(f"[Tracker] {step_type}: {detail}")

    def analyze(self, input_text):
        self.log_step("analyze", input_text)

    def reflect(self, prior_output):
        self.log_step("reflect", prior_output)

    def iterate(self, refinement_detail):
        self.log_step("iterate", refinement_detail)

    def get_chain(self):
        return self.chain

    def reset(self):
        self.chain.clear()
