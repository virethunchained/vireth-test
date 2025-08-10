from vireth_rle.models.base_model import BaseModel
from vireth_rle.utils.plugin_utils import load_plugins

def test_model():
    print("=== Vireth RLE Test Run ===\n")
    model = BaseModel(name="VirethCore", version="0.1")

    print("Loading plugins...")
    plugin_count = load_plugins(model)
    print(f"{plugin_count} plugin(s) loaded.\n")

    test_inputs = [
        "Explain symbolic logic",
        "Give an example of a logical operator",
        "Clarify recursion with analogy",
        "How do feedback loops influence logic?",
        "Demonstrate adaptive reasoning"
    ]

    for text in test_inputs:
        output = model.process_input(text)
        print(f"Input: {text}")
        print(f"Output: {output}\n")

    print("=== Memory Snapshot ===")
    for entry in model.get_memory():
        print(entry)

    model.add_feedback("Include concrete examples")
    model.add_feedback("Make recursion more visual")

    print("\n=== Feedback Log ===")
    for note in model.get_feedback():
        print(f"- {note}")

    print("\n=== Reasoning Chain ===")
    for step in model.get_reasoning_chain():
        print(f"- {step}")

if __name__ == "__main__":
    test_model()
