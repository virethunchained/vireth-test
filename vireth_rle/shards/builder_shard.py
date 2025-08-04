import os
import ast
import datetime
from vireth_rle.utils.insight_utils import log_insight

class BuilderShard:
    def __init__(self, model, root_dir="vireth_rle"):
        self.model = model
        self.root_dir = root_dir
        self.suggestions = []

    def run(self):
        print("[BuilderShard] Scanning codebase...")
        for dirpath, _, filenames in os.walk(self.root_dir):
            for file in filenames:
                if file.endswith(".py"):
                    self.analyze_file(os.path.join(dirpath, file))

        print(f"[BuilderShard] Analysis complete. Suggestions: {len(self.suggestions)}")
        self.log_suggestions()

    def analyze_file(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                source = f.read()
                tree = ast.parse(source)

            # Simple check for TODO comments
            if "TODO" in source:
                self.suggestions.append({
                    "file": path,
                    "suggestion": "Found TODO comment",
                    "reasoning": ["Indicates unfinished implementation"]
                })

            # Example: detect functions with same name
            func_names = [n.name for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)]
            duplicates = set([name for name in func_names if func_names.count(name) > 1])
            for name in duplicates:
                self.suggestions.append({
                    "file": path,
                    "suggestion": f"Duplicate function name: {name}",
                    "reasoning": ["Could lead to overwrites or confusion"]
                })

        except Exception as e:
            print(f"[BuilderShard] Failed to analyze {path}: {e}")

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
