from models.base_model import BaseModel

def main():
    print("Initializing Vireth RLE Core...")
    model = BaseModel(name="VirethCore", version="0.2")

    # Simulate a cycle of input-processing-feedback
    user_inputs = ["What is recursion?", "Refine that", "What should I do next?"]
    feedbacks = ["More detail", "Add context", "Clarify intent"]

    for i, user_input in enumerate(user_inputs):
        output = model.process_input(user_input)
        print(output)
        model.receive_feedback(feedbacks[i])

    print("\nRecent memory:")
    for entry in model.recall():
        print(entry)

    print("\nFeedback log:")
    for fb in model.feedback_log:
        print("-", fb)

if __name__ == "__main__":
    main()
