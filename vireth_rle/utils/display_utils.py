# vireth_rle/utils/display_utils.py

def color_print(text, tag=None, subtype=None, color=None):
    """
    Prints color-coded text to terminal based on tag/subtype or explicit color.
    
    Args:
        text (str): Text to print.
        tag (str): Optional tag (e.g., 'plugin', 'log').
        subtype (str): Optional subtype (e.g., 'emotion', 'insight').
        color (str): Optional direct color override.
    """
    # ANSI escape codes
    COLORS = {
        "gray": "\033[90m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "reset": "\033[0m"
    }

    # Tag/subtype to color mapping
    COLOR_MAP = {
        ("plugin", "emotion"): "yellow",
        ("plugin", "topic"): "magenta",
        ("plugin", "pattern"): "green",
        ("plugin", "insight"): "cyan",
        ("log", "insight"): "cyan",
        ("plugin", None): "gray",
        (None, None): "reset"
    }

    ansi_color = COLORS.get(
        color or COLOR_MAP.get((tag, subtype), "reset"),
        COLORS["reset"]
    )

    print(f"{ansi_color}{text}{COLORS['reset']}")
