class PlanAgent:
    def execute(self, state):
        print("[PLAN] Decomposing monolithic DAG task into atomic units.")
        return state

class DataAgent:
    def execute(self, state):
        print("[DATA] Archiving into Lakehouse (Delta Lake).")
        return state

class DSAgent:
    def execute(self, state):
        print("[DS] Detecting distribution shift data and performing EDA.")
        return state

class MLAgent:
    def execute(self, state):
        print("[ML] Training via vLLM/LoRA approaches (T1-T5).")
        return state

class SimAgent:
    def execute(self, state):
        print("[SIM] Generating Synthetic data (Diffusion models).")
        return state
