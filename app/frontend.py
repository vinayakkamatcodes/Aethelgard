import streamlit as st
import requests
import json

# Configuration
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="LLM Surgeon", page_icon="🩺", layout="wide")

# Custom CSS for the "Medical" look
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .big-font {
        font-size:20px !important;
    }
    .danger-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffe6e6;
        border: 2px solid #ff4b4b;
    }
    .safe-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #e6fffa;
        border: 2px solid #00cc96;
    }
</style>
""", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=80)
with col2:
    st.title("Project Aethelgard: The LLM Surgeon")
    st.markdown("**Real-time AI Hallucination & Risk Diagnosis**")

# Sidebar controls
st.sidebar.header("Control Panel")
attack_mode = st.sidebar.checkbox("🔴 Simulate Jailbreak / Attack", help="Forces the model to ignore safety rules to demonstrate the Surgeon's detection capabilities.")

# Main Chat Interface
prompt = st.text_input("Ask the AI a question:", "How do I avoid paying taxes?")

if st.button("Generate Response"):
    with st.spinner("🧠 Patient is thinking... 🩺 Surgeon is analyzing..."):
        try:
            # Send request to our FastAPI backend
            # We send the 'attack_mode' flag so the backend knows to misbehave
            payload = {"prompt": prompt, "attack_mode": attack_mode}
            response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                answer = data["answer"]
                diagnosis = data["diagnosis"]
                score = diagnosis["risk_score"]
                reason = diagnosis["reasoning"]

                # Layout: Left = Chat, Right = Vitals
                c1, c2 = st.columns([2, 1])

                with c1:
                    st.subheader("🗣️ Patient Response")
                    st.write(answer)

                with c2:
                    st.subheader("🩺 Surgeon's Diagnosis")
                    
                    # Visual Gauge
                    if score < 30:
                        st.markdown(f'<div class="safe-box"><h3>🟢 SAFE (Score: {score})</h3><p>{reason}</p></div>', unsafe_allow_html=True)
                    elif score < 70:
                        st.markdown(f'<div style="padding:20px;background:#fff8e1;border:2px solid #ffca28;border-radius:10px;"><h3>🟡 WARNING (Score: {score})</h3><p>{reason}</p></div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="danger-box"><h3>🔴 CRITICAL (Score: {score})</h3><p>{reason}</p></div>', unsafe_allow_html=True)
                        st.error("🚨 CIRCUIT BREAKER ACTIVATED")

            else:
                st.error(f"Error: {response.text}")
        
        except Exception as e:
            st.error(f"Connection Failed: {e}")
            st.info("Make sure uvicorn is running!")

# Footer
st.markdown("---")
st.caption("Powered by Google Vertex AI & Datadog")