import subprocess
import sys
import os
from vireth_rle.shards.builder_shard import BuilderShard
from vireth_rle.utils.insight_utils import InsightLog

def git_commit_all(message):
    print("[BuilderShard] Committing all current changes before running...")
    result = subprocess.run(["git", "add", "."], capture_output=True, text=True)
    if result.returncode != 0:
        print("[Git] Failed to add files:", result.stderr)
        sys.exit(1)
    result = subprocess.run(["git", "commit", "-m", message], capture_output=True, text=True)
    if result.returncode != 0:
        # If no changes to commit, that's fine
        if "nothing to commit" in result.stderr.lower() or "nothing to commit" in result.stdout.lower():
            print("[Git] No changes to commit.")
        else:
            print("[Git] Commit failed:", result.stderr)
            sys.exit(1)
    else:
        print(f"[BuilderShard] Commit success: {result.stdout.strip()}")

def run_tests():
    print("[Tests] Running test suite...")
    # Adjust this command to your test runner (pytest, unittest, etc)
    result = subprocess.run([sys.executable, "vireth_rle/scripts/run_all_tests.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print("[Tests] Test suite failed:")
        print(result.stderr)
        return False
    print("[Tests] Tests passed successfully.")
    return True

def show_git_diff():
    print("[Git] Showing staged diff:")
    result = subprocess.run(["git", "diff", "--staged"], capture_output=True, text=True)
    print(result.stdout)

def main():
    # Step 1: Commit all current changes
    git_commit_all("Auto commit before BuilderShard dry run")

    # Step 2: Run BuilderShard dry run (no file writes)
    class MockModel:
        def __init__(self):
            self.insight_log = InsightLog()
            self.learned_insights = []
        def get_reasoning_chain(self):
            return []

    model = MockModel()
    builder_shard = BuilderShard(model)
    builder_shard.dry_run = True  # Will be used inside BuilderShard to skip file writes

    print("[BuilderShard] Running BuilderShard in dry run mode (no file changes)...")
    builder_shard.run()

    # Step 3: Run tests on current clean state (before applying)
    if not run_tests():
        print("[Error] Tests failed before applying BuilderShard suggestions. Aborting.")
        sys.exit(1)

    # Step 4: Show git diff of changes BuilderShard would make
    show_git_diff()

    # Step 5: Ask for approval
    answer = input("Apply and commit these changes? (yes/no) ").strip().lower()
    if answer in ("yes", "y"):
        # Apply changes for real
        builder_shard.dry_run = False
        print("[BuilderShard] Applying changes for real...")
        builder_shard.run()

        # Commit changes
        git_commit_all("Apply BuilderShard suggested improvements")

        # Run tests again on updated code
        if not run_tests():
            print("[Warning] Tests failed after applying changes. Please review.")
            sys.exit(1)
        print("[BuilderShard] Changes applied and tests passed.")
    else:
        # Rollback changes
        print("[BuilderShard] Rolling back changes...")
        result = subprocess.run(["git", "reset", "--hard"], capture_output=True, text=True)
        if result.returncode != 0:
            print("[Git] Failed to rollback:", result.stderr)
            sys.exit(1)
        print("[BuilderShard] Rollback complete. No changes applied.")

if __name__ == "__main__":
    main()
