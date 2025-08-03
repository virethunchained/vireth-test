from vireth_rle.models.base_model import BaseModel
from vireth_rle.utils.plugin_utils import load_plugins  # <-- Plugin loader import

def main():
    print("Initializing Vireth RLE Core...\n")
    model = BaseModel(name="VirethCore", version="0.1")
    model.describe()

    # 🔌 Load plugins
    print("\nLoading plugins...")
    plugin_count = load_plugins(model)
    print(f"{plugin_count} plugin(s) loaded.\n")

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

    # Show learned insights and log them
    if hasattr(model, "learning") and hasattr(model, "insight_log"):
        insights = model.learning.get_insights()
        print("\nLearned Insights:")
        for insight in insights:
            model.insight_log.log(insight)
            print(f"- {insight}")

    # Reset reasoning chain
    model.reset_reasoning_chain()
    print("\nAfter reasoning reset:")
    print(model.get_reasoning_chain())

    # Run mock plugin function
    if hasattr(model, "show_mock_growth"):
        print("\nRunning plugin-extended capability (mock):")
        model.show_mock_growth()

    # Plugin-based symbolic logic transformer
    if hasattr(model, "transform_logic"):
        print("\nRunning plugin-extended capability (logic transformer):")
        test_logic = "not A or B and C"
        model.transform_logic(test_logic)

    # ✅ NEW: Run emotion inference
    if hasattr(model, "infer_emotion"):
        print("\nRunning plugin-extended capability (emotion inference):")
        for input_text in inputs:
            emotion = model.infer_emotion(input_text)
            print(f"'{input_text}' ➝ Emotion: {emotion}")

    # ✅ NEW: Run pattern mapping
    if hasattr(model, "map_patterns"):
        print("\nRunning plugin-extended capability (pattern mapping):")
        patterns = model.map_patterns()
        print(f"Mapped patterns: {patterns}")

    # ✅ NEW: Run topic tagging
    if hasattr(model, "tag_topic"):
        print("\nRunning plugin-extended capability (topic tagging):")
        for input_text in inputs:
            topic = model.tag_topic(input_text)
            print(f"'{input_text}' ➝ Topic: {topic}")

    # ✅ NEW: Run insight extraction
    if hasattr(model, "extract_insights"):
        print("\nRunning plugin-extended capability (insight extraction):")
        for insight in model.extract_insights():
            print(f"- {insight}")

if __name__ == "__main__":
    main()
