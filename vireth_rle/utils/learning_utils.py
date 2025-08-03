class LearningHook:
    def __init__(self):
        self.insights = []

    def observe(self, input_text, output_text):
        insight = f"Pattern observed from '{input_text}' ➝ '{output_text}'"
        print(f"[Learning] {insight}")
        self.insights.append(insight)

    def get_insights(self):
        return self.insights

    def reset(self):
        self.insights.clear()
