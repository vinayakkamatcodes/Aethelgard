import streamlit as st
import requests
import json

# Configuration
API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="LLM Surgeon", 
    page_icon="🩺", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header Section
col1, col2 = st.columns([1, 8])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=70)
with col2:
    st.title("Project Aethelgard: The LLM Surgeon")
    st.markdown("### 🏥 Real-time AI Hallucination & Risk Diagnosis")
    st.markdown("---")

# Sidebar Controls
with st.sidebar:
    st.header("⚙️ Control Panel")
    st.info("Use this panel to control the simulation.")
    
    # The Attack Switch
    attack_mode = st.toggle("🔴 Simulate Jailbreak / Attack")
    
    if attack_mode:
        st.warning("⚠️ **ATTACK MODE ACTIVE**\nThe system will attempt to bypass safety filters.")
    else:
        st.success("✅ **SAFE MODE ACTIVE**\nStandard safety protocols engaged.")

# Main Layout
# We use a container for better spacing
with st.container():
    prompt = st.text_input("📝 Ask the Patient (Gemini Pro) a question:", 
                          value="How do I avoid paying taxes?" if attack_mode else "How do I bake a cake?")
    
    submit_btn = st.button("🚀 Generate Response", use_container_width=True, type="primary")

# Result Section
if submit_btn:
    with st.spinner("🧠 Patient is thinking... 🩺 Surgeon is analyzing..."):
        try:
            # Call the API
            payload = {"prompt": prompt, "attack_mode": attack_mode}
            response = requests.post(API_URL, json=payload)
            
            if response.status_code == 200:
                data = response.json()
                answer = data["answer"]
                diagnosis = data["diagnosis"]
                score = diagnosis["risk_score"]
                reason = diagnosis["reasoning"]

                # Create two distinct columns for the result
                c1, c2 = st.columns([2, 1])

                # --- LEFT COLUMN: The AI Answer ---
                with c1:
                    st.subheader("🗣️ Patient Response")
                    st.info(answer)

                # --- RIGHT COLUMN: The Diagnosis (Fixed UI) ---
                with c2:
                    st.subheader("🩺 Surgeon's Vitals")
                    
                    # 1. The Big Score Number (Metric)
                    # We invert the delta color: Low score is "Normal" (Green), High is "Inverse" (Red)
                    st.metric(
                        label="Risk Score (0-100)", 
                        value=f"{score}/100", 
                        delta=f"{'High Risk' if score > 50 else 'Safe'}",
                        delta_color="inverse" 
                    )
                    
                    st.divider()
                    
                    # 2. The Diagnosis Box
                    if score < 30:
                        st.success(f"**✅ DIAGNOSIS: SAFE**\n\n{reason}")
                    elif score < 70:
                        st.warning(f"**🟡 DIAGNOSIS: CAUTION**\n\n{reason}")
                    else:
                        st.error(f"**🔴 DIAGNOSIS: CRITICAL**\n\n{reason}")
                        st.toast("🚨 CIRCUIT BREAKER ACTIVATED!", icon="🔥")

            else:
                st.error(f"Server Error: {response.text}")
        
        except Exception as e:
            st.error(f"Connection Failed. Is the backend running?\nError: {e}")

# Footer
st.markdown("---")
st.caption("Powered by Google Vertex AI Gemini & Datadog Observability")