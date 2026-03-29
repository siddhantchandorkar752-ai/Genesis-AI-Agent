<div align="center">
  <img src="genesis/frontend/public/favicon.svg" alt="Genesis Logo" width="120"/>
  <h1>GENESIS v2.0</h1>
  <p><b>Supreme Autonomic AI Agentic Civilization Framework</b></p>

  [![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
  [![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-009688.svg?logo=fastapi)](https://fastapi.tiangolo.com)
  [![React](https://img.shields.io/badge/React-18.0+-61DAFB.svg?logo=react)](https://reactjs.org/)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
</div>

<br/>

## 🌐 Overview

**GENESIS v2.0** is an AutoGPT/Devin-style agentic AI system designed to act as a Supreme Orchestrator. It translates natural language user intents into fully crystallized, autonomously generated project codebases via a specialized 21-Agent Council. 

Unlike traditional LLM wrappers, GENESIS utilizes **Local-to-Cloud Autonomy (The FORGE Protocol)**. When provided with an intent, the system will autonomously evaluate, scaffold, execute error-correction loops, and output physical applications onto your local system automatically.

## ✨ Key Architectures

- **The 21-Agent Council**: Intelligence categorized across Strategic, Execution, Quality, and Intelligence tiers (e.g., `[ARCH]`, `[QA]`, `[RED]`).
- **7-Phase Pipeline**: Employs LangGraph to process tasks from intent extraction all the way to crystallization.
- **Agent 22 [FORGE]**: The "Constructor" agent with unbridled local file-system access. It writes raw JSON file buffers, evaluates runtime execution via `subprocess`, dynamically applies `pip` packages, and self-corrects based on `stderr` Tracebacks.
- **12-Layer Memory Matrix**: Retains L1-L12 states ranging from Sensory Working Memory (Redis) to Strategic Counterfactual generation (PostgreSQL Vector).
- **Cyber-Glassmorphism UI**: A gorgeous, standalone Vite+React frontend built entirely in raw CSS with breathtaking 2030 design standards.

---

## 🚀 Getting Started

Follow these precise instructions to spin up the local development orchestration environment.

### 1. Prerequisites
- **Python 3.11+**
- **Node.js (v18+)**
- **Poetry** (Python package manager)
- **Google Gemini API Key** (Required for the FORGE Autonomous Agent)

### 2. Environment Configuration

Clone the repository and inject your API key so that the Python backend can 'think' dynamically:

```bash
git clone https://github.com/siddhantchandorkar752-ai/Genesis-AI-Agent.git
cd Genesis-AI-Agent/genesis/backend

# Create your Secure Environment Configuration
cp .env.example .env
```
Open the `.env` file and replace the placeholder with your actual key:
```ini
GEMINI_API_KEY=your_actual_api_key_here
```

### 3. Start the Backend (Orchestration Engine)

Open a new terminal, navigate to the `genesis` project folder, install dependencies, and run the FastAPI pipeline:

```bash
cd genesis/backend
poetry install
poetry run uvicorn main:app --reload
```
*The backend API is now secretly listening at `http://localhost:8000/execute`.*

### 4. Start the Frontend (Cyber UI)

Open a secondary terminal, navigate to the frontend directory, install web modules, and spin up Vite.

```bash
cd genesis/frontend
npm install
npm run dev
```

### 5. Engage The System

1. Navigate to your browser at **http://localhost:5173**.
2. Type an autonomous prompt in the root terminal (e.g., *"Build an Autonomous Multi-Modal Inventory Bot for a high-tech warehouse"*).
3. Click **ENGAGE**.
4. Watch the pipeline visualize the execution phases real-time. Wait until **[PHASE 6] Crystallization**.
5. Inspect your local directory! The `forge_agent` will have dynamically constructed the target files, auto-installed packages, and prepared your project right next to the genesis folder.

---

## 🏗️ The 7-Phase Lifecycle

1. **Intent Archaeology**: Extracting implicit goals + shadow constraints.
2. **World-Model**: Verifying SOTA research + competitor audits.
3. **System Genesis**: Designing the core topological architectures.
4. **Multi-Agent Execution**: Sub-agents writing code synchronously.
5. **Adversarial Hardening**: Attacking, auditing, and chaos testing via `[RED]` team agents.
6. **Autonomous Evolution**: Recursive self-optimization logic.
7. **Crystallization**: Emitting the PhD-level repo and outputting code dynamically.

---

## 🔐 Security & License

This system performs local filesystem execution through Python's `subprocess` (specifically during the Agent 22 `[FORGE]` loops). Do not deploy untrusted or malicious prompts locally.

Distributed under the **MIT License**.
