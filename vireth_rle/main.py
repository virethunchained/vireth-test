from vireth_rle.models.base_model import BaseModel

def main():
    print("Initializing Vireth RLE Core...\n")
    model = BaseModel(name="VirethCore", version="0.1")
    model.describe()

    # Simulated training prompts
    inputs = [
        "Explain symbolic logic",
        "Give an example",
        "Clarify recursion in your answer",
        "What else can you derive?"
    ]

    for user_input in inputs:
        output = model.process_input(user_input)
        print(output)

    # Show memory buffer
    print("\nMemory snapshot:")
    for entry in model.get_memory():
        print(entry)

    # Simulate adding feedback
    model.feedback.add("Be more concise")
    model.feedback.add("Add illustrative examples")
    model.feedback.add("Avoid circular definitions")

    # Show feedback log
    print("\nFeedback log:")
    for item in model.feedback.show():
        print(f"- {item}")

if __name__ == "__main__":
    main()
