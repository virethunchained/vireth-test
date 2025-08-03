# vireth_rle/utils/feedback_utils.py

class FeedbackLog:
    def __init__(self):
        self.log = []

    def add_feedback(self, feedback):
        print(f"Logging feedback: {feedback}")
        self.log.append(feedback)

    def get_all_feedback(self):
        return self.log
