from vireth_rle.utils.recursive_utils import RecursiveChainTracker

def test_tracker():
    tracker = RecursiveChainTracker()

    tracker.log_step("analyze", "Interpreting symbolic logic")
    tracker.log_step("reflect", "Evaluating previous reasoning")
    tracker.log_step("iterate", "Refined question based on context")

    print("\nFull Reasoning Chain:")
    for step in tracker.get_chain():
        print(f"- {step['step']}: {step['detail']}")

    tracker.reset()
    print("\nAfter reset:")
    print(tracker.get_chain())

if __name__ == "__main__":
    test_tracker()
