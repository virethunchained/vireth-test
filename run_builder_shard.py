from vireth_rle.models.base_model import BaseModel
from vireth_rle.shards.builder_shard import BuilderShard
from vireth_rle.utils.insight_utils import log_insight

# Initialize the core model
model = BaseModel(name="Vireth RLE", version="0.3")

# Initialize and run the Builder Shard
shard = BuilderShard(model=model, root_dir="vireth_rle")
shard.run()

# Print all logged suggestions
print("\n--- Logged Suggestions ---")
insights = model.get_logged_insights()
for idx, insight in enumerate(insights):
    print(f"\nSuggestion {idx + 1}:")
    for key, value in insight.items():
        print(f"{key}: {value}")
