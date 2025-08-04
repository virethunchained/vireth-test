import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from vireth_rle.models.base_model import BaseModel
from vireth_rle.plugins.emotion_inference_plugin import register as register_emotion
from vireth_rle.plugins.topic_tagger_plugin import register as register_topic
from vireth_rle.plugins.pattern_mapper_plugin import register as register_pattern
from vireth_rle.plugins.insight_extractor_plugin import register as register_insight

# Step 1: Create model instance
model = BaseModel(name="Vireth RLE", version="0.3")

# Step 2: Register all emergent plugins
register_emotion(model)
register_topic(model)
register_pattern(model)
register_insight(model)

# Step 3: Feed test input
input_text = "I'm frustrated with how people keep ignoring symbolic logic. It’s foundational to reasoning."
output = model.process_input(input_text)

# Step 4: Print output
print("\n--- Model Output ---")
print(output)

# Step 5: Get and print insights
insights = model.get_logged_insights()
print(f"\nTotal insights logged: {len(insights)}")

print("\n--- Logged Insight(s) ---")
for idx, insight in enumerate(insights):
    print(f"\nInsight {idx + 1}:")
    for key, value in insight.items():
        print(f"{key}: {value}")

