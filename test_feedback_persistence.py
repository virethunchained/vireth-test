from vireth_rle.models.base_model import BaseModel

model = BaseModel("Vireth", "0.3")

# Add sample feedback
model.add_feedback("Try simplifying recursive logic in chain_tracker.")
model.add_feedback("Insight logging works well, consider abstracting formatter.")

# Print all stored feedback
print("\n--- Logged Feedback ---")
for f in model.get_feedback():
    print("-", f)
