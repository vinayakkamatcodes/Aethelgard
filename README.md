# 🩺 Project Aethelgard: The LLM Surgeon

> **Winner of the Google Cloud x Datadog Hackathon 2025 (Candidate)**
> *Transforming LLM Observability from Passive Monitoring to Active Diagnosis.*

![Python](https://img.shields.io/badge/Python-3.10-blue) ![FastAPI](https://img.shields.io/badge/FastAPI-High%20Performance-green) ![Gemini](https://img.shields.io/badge/AI-Vertex%20AI%20Gemini-orange) ![Datadog](https://img.shields.io/badge/Observability-Datadog-purple)

## 🚨 The Problem
Large Language Models (LLMs) are "Black Boxes." When they hallucinate or give dangerous advice in high-stakes industries (Finance, Healthcare), standard monitoring tools fail. They tell you *that* an error happened (500 Internal Error), but they don't tell you **why** the model lied or how confident it was.

## 💡 The Solution: "The Digital Autopsy"
**Project Aethelgard** is an AI Governance Gateway that sits between your users and your LLM. It acts as a **Real-Time Surgeon**:

1.  **The Patient (Gemini Pro):** Generates the response.
2.  **The Surgeon (Gemini Flash):** A specialized, temperature-0 model that performs a "Live MRI" on the answer. It grades factual accuracy and safety (0-100) before the user even sees it.
3.  **The Monitor (Datadog):** We stream these "Risk Scores" to Datadog. If the risk spikes, we visualize the "Heartbeat" of the model in real-time.

---

## 📸 Screenshots

### 1. The "Attack" Simulation
*We forced the model to generate illegal advice. The Surgeon caught it instantly.*
![Streamlit Interface](https://via.placeholder.com/800x400?text=Insert+Screenshot+of+Red+Streamlit+Here)

### 2. The Datadog "Heartbeat"
*Real-time visualization of the Hallucination Spike in Datadog.*
![Datadog Dashboard](https://via.placeholder.com/800x400?text=Insert+Screenshot+of+Datadog+Graph+Here)

---

## 🏗️ Architecture

```mermaid
graph LR
    A[User Request] --> B(FastAPI Gateway)
    B --> C{The Patient<br>Gemini Pro}
    C --> D[Generated Answer]
    D --> E{The Surgeon<br>Gemini Flash}
    E --> F[Risk Score Calculation]
    F --> G((Datadog Agent))
    G --> H[Dashboard Alert]
    F --> B
    B --> I[Frontend UI]

🛠️ Tech Stack

    Orchestration: Python FastAPI

    GenAI: Google Vertex AI (Gemini Pro & Gemini 1.5 Flash)

    Observability: Datadog (DogStatsD, Custom Metrics)

    Frontend: Streamlit

⚡ Key Features

    🛡️ Semantic Guardrails: We don't just use Regex. We use a secondary LLM to semantically understand if an answer is dangerous.

    📉 Real-Time Risk Telemetry: Emits llm.surgeon.risk_score metric to Datadog via UDP.

    🔴 Attack Simulation Mode: A built-in "Jailbreak" button to demonstrate the system's resilience for judges.

🚀 How to Run
1. Prerequisites

    Python 3.10+

    Datadog Agent installed (Listening on port 8125)

    Google Cloud Service Account

2. Installation
    # Clone the repo
    git clone [https://github.com/your-username/llm-surgeon.git](https://github.com/your-username/llm-surgeon.git)

    # Install dependencies
    pip install -r requirements.txt

3. Start the System
    # Terminal 1: Start the API Backend
    uvicorn app.main:app --reload

    # Terminal 2: Start the Frontend
    streamlit run app/frontend.py

4.View in Datadog

    Go to Metrics Explorer and search for: llm.surgeon.risk_score

🎥 Video Demo

[Link to YouTube Video]
