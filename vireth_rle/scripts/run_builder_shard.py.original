from vireth_rle.shards.builder_shard import BuilderShard
from vireth_rle.utils.insight_utils import InsightLog

# Mock model for testing
class MockModel:
    def __init__(self):
        self.insight_log = InsightLog()   # Use InsightLog instance, not list
        self.learned_insights = []

    def get_reasoning_chain(self):
        return []

model = MockModel()

builder_shard = BuilderShard(model)
builder_shard.run()
