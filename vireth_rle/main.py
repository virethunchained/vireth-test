from vireth_rle.models.base_model import BaseModel


def main():
    print("Initializing Vireth RLE Core...\n")
    model = BaseModel(name="VirethCore", version="0.1")
    model.describe()

    # Simulate input loop
    inputs = [
        "Explain symbolic logic",
        "Give an example",
        "Clarify recursion in your answer",
        "What else can you derive?"
    ]

    for user_input in inputs:
        output = model.process_input(user_input)
        print(output)

    # Display memory
    print("\nMemory snapshot:")
    for entry in model.get_memory():
        print(entry)

    # Add feedback examples
    model.add_feedback("Be more concise")
    model.add_feedback("Add illustrative examples")
    model.add_feedback("Avoid circular definitions")

    # Display feedback
    print("\nFeedback log:")
    for note in model.get_feedback():
        print(f"- {note}")

    # Show reasoning chain
    print("\nReasoning Chain:")
    for step in model.get_reasoning_chain():
        print(f"- {step}")

    # Reset reasoning chain
    model.reset_reasoning_chain()
    print("\nAfter reasoning reset:")
    print(model.get_reasoning_chain())

if __name__ == "__main__":
    main()
