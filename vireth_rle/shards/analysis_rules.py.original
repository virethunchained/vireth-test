import ast

def check_all(source_code, path):
    """
    Run all analysis rules on the given source code string.
    Returns a list of dict suggestions.
    """

    suggestions = []
    try:
        tree = ast.parse(source_code)
    except Exception as e:
        suggestions.append({
            "file": path,
            "line": None,
            "suggestion": f"Failed to parse file: {e}",
            "reasoning": ["Syntax error or invalid Python code"]
        })
        return suggestions

    # Rule 1: Detect TODO or FIXME comments
    lines = source_code.splitlines()
    for i, line in enumerate(lines, start=1):
        if "TODO" in line or "FIXME" in line:
            suggestions.append({
                "file": path,
                "line": i,
                "suggestion": "Found TODO/FIXME comment",
                "reasoning": ["Indicates unfinished work or issues"]
            })

    # Rule 2: Detect functions with too many arguments (>5)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if len(node.args.args) > 5:
                suggestions.append({
                    "file": path,
                    "line": node.lineno,
                    "suggestion": f"Function '{node.name}' has too many arguments ({len(node.args.args)})",
                    "reasoning": ["Functions with many arguments are harder to maintain"]
                })

    # Rule 3: Detect functions longer than 50 lines
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if hasattr(node, "body") and len(node.body) > 50:
                suggestions.append({
                    "file": path,
                    "line": node.lineno,
                    "suggestion": f"Function '{node.name}' is too long ({len(node.body)} lines)",
                    "reasoning": ["Long functions should be broken down"]
                })

    # Rule 4: Detect unused imports (simple heuristic)
    imported_names = set()
    used_names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported_names.add(alias.asname or alias.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                imported_names.add(alias.asname or alias.name)
        elif isinstance(node, ast.Name):
            used_names.add(node.id)
    unused = imported_names - used_names
    for name in unused:
        suggestions.append({
            "file": path,
            "line": None,
            "suggestion": f"Unused import '{name}'",
            "reasoning": ["Removing unused imports cleans code and reduces clutter"]
        })

    # Rule 5: Simple cyclomatic complexity estimator (counts branches)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            complexity = 1  # default for function entry
            for subnode in ast.walk(node):
                if isinstance(subnode, (ast.If, ast.For, ast.While, ast.And, ast.Or, ast.ExceptHandler)):
                    complexity += 1
            if complexity > 10:
                suggestions.append({
                    "file": path,
                    "line": node.lineno,
                    "suggestion": f"Function '{node.name}' is too complex (cyclomatic complexity ~{complexity})",
                    "reasoning": ["High complexity functions are harder to maintain and test"]
                })

    # Rule 6: Functions missing docstrings
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if not ast.get_docstring(node):
                suggestions.append({
                    "file": path,
                    "line": node.lineno,
                    "suggestion": f"Function '{node.name}' is missing a docstring",
                    "reasoning": ["Docstrings improve code documentation and readability"]
                })

    return suggestions
