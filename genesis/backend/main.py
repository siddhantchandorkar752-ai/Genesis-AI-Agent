from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.orchestrator import run_genesis_pipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="GENESIS v2.0 System Architect",
    description="The Supreme AI System Architect - Recursive & Self-Correcting",
    version="2.0.0"
)

class IntentRequest(BaseModel):
    intent: str
    constraints: dict = {}

@app.post("/execute")
async def execute_intent(request: IntentRequest):
    logger.info(f"[GENESIS] Received Intent: {request.intent}")
    try:
        # Phase 0-6 orchestration
        final_state = run_genesis_pipeline(request.intent, request.constraints)
        return {"status": "success", "result": final_state}
    except Exception as e:
        logger.error(f"[CHAOS] Pipeline Failure: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health_check():
    return {"status": "GENESIS ONLINE", "agents": 21, "memory_layers": 12}
