# Phase 6 Generated: Neurosymbolic Logic Engine
class LogicEngine:
    def evaluate(self, yolo_conf, vlm_reasoning):
        """
        Neural inputs (conf, reasoning strings) are evaluated
        by hard-coded symbolic logic safety checks.
        """
        if yolo_conf > 0.95 and "crushed" in vlm_reasoning.lower():
            return {
                "action": "DISCARD",
                "explain": f"Discarding item. Neural confidence is {yolo_conf*100}%. Symbolic logic flagged VLM reason: '{vlm_reasoning}'."
            }
        
        if yolo_conf < 0.50:
            return {
                "action": "ALERT_HUMAN",
                "explain": "Robot is confused. YOLO sensor confidence is too low to proceed."
            }
            
        return {"action": "KEEP", "explain": "Item passes Neurosymbolic QA."}
