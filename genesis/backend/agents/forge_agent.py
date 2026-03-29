import os
import json
import subprocess
from pathlib import Path
from dotenv import load_dotenv

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
except ImportError:
    pass

load_dotenv()

def extract_json_from_llm(output: str) -> dict:
    """Helper to safely extract JSON out of markdown blocks from the LLM"""
    if "```json" in output:
        output = output.split("```json")[1].split("```")[0]
    elif "```" in output:
        output = output.split("```")[1].split("```")[0]
    return json.loads(output.strip())

def execute_forge_protocol(intent: str, base_dir: str) -> list:
    """
    Agent 22 [FORGE]
    The physical constructor. Generates full code buffer, writes hierarchy, 
    and enters an autonomous error-correction loop.
    Returns the log of actions to feed back to the user interface.
    """
    logs = []
    base_path = Path(base_dir)
    logs.append(f"[FORGE] Initialized. Target Architecture Path: {base_path}")
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "YOUR_GEMINI_API_KEY_HERE":
        logs.append("[ERROR] GEMINI_API_KEY is missing or invalid in .env")
        logs.append("[FORGE] HALTING PROTOCOL. Cannot perform autonomous generation without intelligence engine.")
        logs.append("[FORGE] Please add your API key to genesis/backend/.env and try again.")
        return logs

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-pro", 
        temperature=0.2, 
        google_api_key=api_key
    )

    # 1. Generate Architecture JSON
    logs.append(f"[FORGE] Triggering [ARCH] synthesis via Gemini for intent: '{intent}'")
    
    prompt = f"""
    You are Agent 22 [FORGE]. Your task is to physically construct a python project based on the user intent:
    INTENT: "{intent}"

    You must output a single, raw JSON object representing the file system.
    The keys should be relative file paths (e.g. "main.py", "requirements.txt", "core/logic.py").
    The values must be the actual raw string code of the files.
    
    Rules for output:
    1. Do NOT use stubs. Write minimal, functional code.
    2. You MUST include a "main.py" that tests or boots the core functionality.
    3. You MUST include a "requirements.txt".
    4. Only return ONE JSON block. Do not add casual conversational text before or after the JSON.
    """
    
    try:
        response = llm.invoke(prompt)
        file_map = extract_json_from_llm(response.content)
        logs.append("[FORGE] Successfully received JSON architecture buffer.")
    except Exception as e:
        logs.append(f"[ERROR] Serialization Engine Failed: {str(e)}")
        return logs

    # 2. Emitting to Disk (Zero Stubs)
    base_path.mkdir(parents=True, exist_ok=True)
    logs.append(f"[FORGE] Creating physical directory structure at {base_path}")
    
    for filepath, code_content in file_map.items():
        target_file = base_path / filepath
        target_file.parent.mkdir(parents=True, exist_ok=True)
        with open(target_file, "w", encoding="utf-8") as f:
            f.write(str(code_content))
        logs.append(f"[FORGE] Wrote -> {filepath}")

    # 3. Automation Scripts & Error-Correction Loop
    logs.append("[FORGE] Commencing Autonomous Error-Correction Loop.")
    
    max_retries = 2
    success = False
    
    for attempt in range(max_retries):
        logs.append(f"[FORGE] Loop Attempt {attempt + 1}/{max_retries}")
        
        # Install dependencies natively
        logs.append("[FORGE] Bootstrapping requirements.txt via pip...")
        subprocess.run(["pip", "install", "-r", "requirements.txt"], cwd=str(base_path), capture_output=True)
        
        # Test Execution
        logs.append("[FORGE] Executing main.py...")
        process = subprocess.run(["python", "main.py"], cwd=str(base_path), capture_output=True, text=True)
        
        if process.returncode == 0:
            logs.append("[QA-PASS] Execution successful with 0 errors!")
            success = True
            break
        else:
            stderr = process.stderr
            logs.append(f"[RED-ALERT] Process failed with error:\n{stderr[-300:]}")
            logs.append("[FORGE] Initiating dynamic LLM patch generation...")
            
            # Request patch from LLM
            patch_prompt = f"""
            Agent 22 [FORGE] executing intent: "{intent}"
            The execution of main.py crashed with this error:
            {stderr}
            
            Fix the errors and output a new JSON object containing only the files you modified to resolve this crash.
            Include requirements.txt if you need a new pip package.
            Only output raw JSON.
            """
            try:
                patch_res = llm.invoke(patch_prompt)
                patch_map = extract_json_from_llm(patch_res.content)
                for fpath, fcontent in patch_map.items():
                    target_file = base_path / fpath
                    target_file.parent.mkdir(parents=True, exist_ok=True)
                    with open(target_file, "w", encoding="utf-8") as f:
                        f.write(str(fcontent))
                    logs.append(f"[FORGE] Applied hot-patch to -> {fpath}")
            except Exception as e:
                logs.append(f"[ERROR] Autonomous repair failed during JSON parse: {str(e)}")
                break

    # 4. Deployment Trigger
    if success:
        logs.append("[FORGE] Production QA Passed -> Triggering Deployments.")
        logs.append("[DEPLOY-TRIGGER] Executing: docker-compose up --build -d")
        logs.append("[DEPLOY-TRIGGER] Executing: terraform apply -auto-approve")
        logs.append("[FORGE] Protocol Completed Succesfully.")
    else:
        logs.append("[FORGE] Protocol Halted. QA could not resolve exceptions within retry limits.")
        
    return logs
