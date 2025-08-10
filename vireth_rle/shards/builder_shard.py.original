import os
import ast
import datetime
from vireth_rle.utils.insight_utils import log_insight
from vireth_rle.utils.file_utils import get_all_py_files_in_dir, read_file, write_file, create_snapshot
from vireth_rle.utils.git_utils import commit_all_changes
from vireth_rle.shards import analysis_rules  # Import our new rules module

class BuilderShard:
    def __init__(self, model, root_dir="vireth_rle"):
        self.model = model
        self.root_dir = root_dir
        self.suggestions = []
        self.file_snapshots = {}
        self.dry_run = False  # Set True to skip writes

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
            source = read_file(path)
            if not source:
                return

            # Parse AST once
            tree = ast.parse(source)

            # Create snapshot only if not dry run
            if not self.dry_run and path not in self.file_snapshots:
                snapshot_path = create_snapshot(path, source)
                self.file_snapshots[path] = snapshot_path

            # Run all analysis rules and collect suggestions
            rules_suggestions = analysis_rules.check_all(source, path)  # FIXED: pass path, not tree

            # Add file path to each suggestion and append
            for sug in rules_suggestions:
                sug.setdefault("file", path)
                self.suggestions.append(sug)

            # Call apply_improvements (placeholder)
            self.apply_improvements(path, source)

        except Exception as e:
            print(f"[BuilderShard] Failed to analyze {path}: {e}")

    def apply_improvements(self, path, original_content):
        if self.dry_run:
            # Dry run: just note the would-be change
            self.suggestions.append({
                "file": path,
                "suggestion": "Dry run - no file changes applied",
                "reasoning": ["Dry run mode active"]
            })
            return

        # Placeholder for future automatic refactor
        # Currently no actual content changes done here
        pass

    def log_suggestions(self):
        for item in self.suggestions:
            text = f"[BuilderShard Suggestion]"
            if "line" in item:
                text += f" (line {item['line']})"
            text += f" {item['suggestion']} in {item['file']}"

            log_insight(
                self.model,
                text=text,
                topic="BuilderShard",
                emotion="neutral",
                patterns=["refactor-suggestion"],
                reasoning=item.get("reasoning", []),
                timestamp=datetime.datetime.utcnow().isoformat()
            )
