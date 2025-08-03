# Vireth RLE (Recursive Learning Engine)

**Vireth** is an adaptive, modular AI prototype designed for recursive reasoning, symbolic logic interpretation, and dynamic growth via plugins.

> **Version:** 0.1  
> **Status:** Early development (Week 2 complete)  
> **Lead Architect:** Non

## 🚀 How to Run

### Prerequisites
- Python 3.8+
- WSL or Linux environment
- Installed at: `~/vireth-test/`

### Run Main Engine
```bash
PYTHONPATH=. python3 -m vireth_rle.main

### Run Batch Test
```bash
PYTHONPATH=. python3 vireth_rle/scripts/test_run.py

📁 Directory Structure
vireth_rle/
├── main.py                     # Entry point for running the RLE core
├── models/
│   └── base_model.py           # Core model class
├── utils/
│   ├── config.py               # Configuration management
│   ├── memory_utils.py         # Memory system
│   ├── feedback_utils.py       # Feedback logging
│   ├── recursive_utils.py      # Reasoning and recursion logic
│   └── plugin_utils.py         # Plugin loading system
├── plugins/
│   └── mock_learning_plugin.py # Example plugin for dynamic extension
└── scripts/
    └── test_run.py             # Batch test runner

✅ Current Features (Week 1–2)
Memory System – Temporarily stores user inputs and outputs

Feedback Log – Tracks feedback notes for future learning refinement

Recursive Thinking Hooks – Basic recursion via RecursiveReasoner and RecursiveChainTracker

Plugin Loader – Dynamically loads modules from /plugins/ that define a register(model) method

Simulated Growth Plugin – Demonstrates Vireth's ability to expand behavior at runtime

Batch Test Script – Automates interactions and logs memory, feedback, and reasoning chains

🧠 What’s Coming in Week 3 (Preview)
Emergent Learning System – Implement learning_utils.py to begin capturing structured insights from input/output behavior

Insight Logging – Automatically detect patterns or lessons from recursive output

Plugin Capability Expansion – Add real-world plugins (e.g., logic transformers, data filters, relevance scorers)

Improved Testing Coverage – Broader scripted test cases to validate core behaviors and emergent logic

