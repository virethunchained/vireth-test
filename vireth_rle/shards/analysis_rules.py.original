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

    return suggestions
