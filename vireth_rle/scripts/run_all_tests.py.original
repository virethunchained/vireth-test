# vireth_rle/scripts/run_all_tests.py
import importlib
import traceback

# List all test modules with relative import paths
test_modules = [
    "test",  # root test.py
    "test_feedback_persistence",
    "test_insight_capture",
    "vireth_rle.scripts.test_recursive_tracker",
    "vireth_rle.scripts.test_run",
]

def run_tests():
    all_passed = True
    for mod_name in test_modules:
        print(f"[TestRunner] Running tests in {mod_name}...")
        try:
            module = importlib.import_module(mod_name)
            for attr in dir(module):
                if attr.startswith("test_"):
                    print(f" - Running {attr}()")
                    func = getattr(module, attr)
                    func()
            print(f"[TestRunner] {mod_name} passed.\n")
        except Exception:
            print(f"[TestRunner] {mod_name} failed:")
            traceback.print_exc()
            all_passed = False
    return all_passed

if __name__ == "__main__":
    success = run_tests()
    if success:
        print("[TestRunner] All tests passed.")
    else:
        print("[TestRunner] Some tests failed.")
