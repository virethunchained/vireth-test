import os
import ast
import datetime
from vireth_rle.utils.insight_utils import log_insight
from vireth_rle.utils.file_utils import get_all_py_files_in_dir, read_file, write_file, create_snapshot
from vireth_rle.utils.git_utils import commit_all_changes

class BuilderShard:
    def __init__(self, model, root_dir="vireth_rle"):
        self.model = model
        self.root_dir = root_dir
        self.suggestions = []
        self.file_snapshots = {}
        self.dry_run = False  # Set to True to enable dry run (no writes)

    def run(self):
        print("[BuilderShard] Committing all current changes before running...")
        success, output = commit_all_changes(commit_message="Auto commit before BuilderShard run")
        if success:
            print(f"[BuilderShard] Commit success: {output}")
        else:
            print(f"[BuilderShard] Commit failed or nothing to commit: {output}")

        print("[BuilderShard] Scanning codebase...")
        py_files = get_all_py_files_in_dir(self.root_dir)
        for file in py_files:
            self.analyze_file(file)

        print(f"[BuilderShard] Analysis complete. Suggestions: {len(self.suggestions)}")
        self.log_suggestions()

    def analyze_file(self, path):
        try:
            # Read the file content
            source = read_file(path)
            if not source:
                return

            # Create a snapshot of the original file state
            if path not in self.file_snapshots:
                snapshot_path = create_snapshot(path, source)
                self.file_snapshots[path] = snapshot_path

            tree = ast.parse(source)

            # Check for 'Refactor this section for better performance.' comments
            if "Refactor this section for better performance." in source:
                self.suggestions.append({
                    "file": path,
                    "suggestion": "Found Refactor this section for better performance. comment",
                    "reasoning": ["Indicates unfinished implementation"]
                })

            # Check for duplicate function names
            func_names = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
            duplicates = set([name for name in func_names if func_names.count(name) > 1])
            for name in duplicates:
                self.suggestions.append({
                    "file": path,
                    "suggestion": f"Duplicate function name: {name}",
                    "reasoning": ["Could lead to overwrites or confusion"]
                })

            # Apply improvements (or dry run)
            self.apply_improvements(path, source)

        except Exception as e:
            print(f"[BuilderShard] Failed to analyze {path}: {e}")

    def apply_improvements(self, path, original_content):
        if self.dry_run:
            # Dry run mode: don't write changes, just record what would be done
            self.suggestions.append({
                "file": path,
                "suggestion": "Would replace 'Refactor this section for better performance.' with refactor suggestion (dry run)",
                "reasoning": ["Dry run - no changes made"]
            })
            return

        # Actual replacement (currently trivial, can be expanded)
        new_content = original_content.replace(
            "Refactor this section for better performance.",
            "Refactor this section for better performance."
        )

        # Write changes back to file
        write_file(path, new_content)

        # Log the improvement
        self.suggestions.append({
            "file": path,
            "suggestion": "Replaced Refactor this section for better performance. with refactor suggestion",
            "reasoning": ["Improves code quality"]
        })

    def log_suggestions(self):
        for item in self.suggestions:
            log_insight(
                self.model,
                text=f"[BuilderShard Suggestion] {item['suggestion']} in {item['file']}",
                topic="BuilderShard",
                emotion="neutral",
                patterns=["refactor-suggestion"],
                reasoning=item["reasoning"],
                timestamp=datetime.datetime.utcnow().isoformat()
            )
