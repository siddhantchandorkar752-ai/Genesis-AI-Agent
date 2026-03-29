import redis
import os
import json
from enum import Enum

class MemoryTier(Enum):
    L01_SENSORY = "l1_sensory"
    L02_WORKING = "l2_working"
    L03_EPISODIC = "l3_episodic"
    L04_SEMANTIC = "l4_semantic"
    L05_PROCEDURAL = "l5_procedural"
    L06_EXPERIMENT = "l6_experiment"
    L07_ERROR = "l7_error"
    L08_OPTIMIZATION = "l8_optimization"
    L09_GRAPH = "l9_graph"
    L10_COUNTERFACTUAL = "l10_counterfactual"
    L11_STRATEGIC = "l11_strategic"
    L12_COLLECTIVE = "l12_collective"

class memory_manager:
    """Manages the 12-layer memory architecture via Redis and Postgres (mocked here)."""
    
    def __init__(self):
        redis_host = os.getenv("REDIS_HOST", "localhost")
        redis_port = int(os.getenv("REDIS_PORT", 6379))
        
        try:
            self.redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)
            self.redis_client.ping()
        except redis.ConnectionError:
            self.redis_client = None
            print("[WARNING] Redis not available, using in-memory mock dict fallback.")
            self.mock_db = {}

    def write_memory(self, tier: MemoryTier, key: str, value: dict):
        data = json.dumps(value)
        db_key = f"{tier.value}:{key}"
        
        if self.redis_client:
            self.redis_client.set(db_key, data)
        else:
            self.mock_db[db_key] = data

    def read_memory(self, tier: MemoryTier, key: str) -> dict:
        db_key = f"{tier.value}:{key}"
        if self.redis_client:
            data = self.redis_client.get(db_key)
        else:
            data = self.mock_db.get(db_key)
            
        if data:
            return json.loads(data)
        return {}

memory_bank = memory_manager()
