import os

def get_all_py_files_in_dir(root_dir):
    """Recursively fetches all Python files in the given directory."""
    py_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if file.endswith(".py"):
                py_files.append(os.path.join(dirpath, file))
    return py_files

def read_file(file_path):
    """Reads the content of a file and returns it."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def write_file(file_path, content):
    """Writes content to a file."""
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
    except Exception as e:
        print(f"Error writing to {file_path}: {e}")

def create_snapshot(file_path, content):
    """Creates a snapshot of the original content to remember for later."""
    snapshot_path = f"{file_path}.original"
    write_file(snapshot_path, content)
    return snapshot_path
