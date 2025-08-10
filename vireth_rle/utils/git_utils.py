import subprocess
import datetime

def run_git_command(args, cwd="."):
    """Run a git command with the given args list and return (success, output)."""
    try:
        result = subprocess.run(
            ["git"] + args,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()

def commit_all_changes(commit_message=None, cwd="."):
    """Stage all changes and commit with a message."""
    success, output = run_git_command(["add", "."], cwd)
    if not success:
        return False, f"Git add failed: {output}"

    if commit_message is None:
        commit_message = f"Auto-commit by BuilderShard at {datetime.datetime.utcnow().isoformat()}"

    success, output = run_git_command(["commit", "-m", commit_message], cwd)
    if not success:
        # Could be "nothing to commit" - treat as success in that case
        if "nothing to commit" in output.lower():
            return True, "No changes to commit."
        return False, f"Git commit failed: {output}"

    return True, output

def get_current_branch(cwd="."):
    """Return the current git branch name."""
    success, output = run_git_command(["rev-parse", "--abbrev-ref", "HEAD"], cwd)
    if success:
        return output
    return None

def create_branch(branch_name, cwd="."):
    """Create a new branch with the given name."""
    success, output = run_git_command(["checkout", "-b", branch_name], cwd)
    return success, output

def rollback_to_commit(commit_hash, cwd="."):
    """Reset the repo to a specific commit hash (hard reset)."""
    success, output = run_git_command(["reset", "--hard", commit_hash], cwd)
    return success, output

def get_latest_commit_hash(cwd="."):
    """Get the latest commit hash on current branch."""
    success, output = run_git_command(["rev-parse", "HEAD"], cwd)
    if success:
        return output
    return None
