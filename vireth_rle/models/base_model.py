class BaseModel:
    def __init__(self, name, version):
        self.name = name
        self.version = version
        self.memory = []            # Stores inputs & outputs
        self.feedback_log = []      # Stores feedback responses

    def describe(self):
        print(f"Model Name: {self.name}")
        print(f"Version: {self.version}")
        print("Memory Slots:", len(self.memory))
        print("Feedback Entries:", len(self.feedback_log))

    def process_input(self, user_input):
        response = f"Processed input: {user_input}"
        self.memory.append({'input': user_input, 'output': response})
        return response

    def receive_feedback(self, feedback):
        self.feedback_log.append(feedback)

    def recall(self):
        return self.memory[-5:]  # Last 5 entries for simplicity
