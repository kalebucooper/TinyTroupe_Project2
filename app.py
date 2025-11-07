import os
from dotenv import load_dotenv
load_dotenv()  # Automatically read .env if present

# ✅ Auto-set your OpenAI API key (safe local fallback)
if "OPENAI_API_KEY" not in os.environ or not os.environ["OPENAI_API_KEY"]:
    os.environ["OPENAI_API_KEY"] = "sk-your-real-api-key-here"  # Replace with your real key

import streamlit as st
from simulation_manager import run_simulation

# =====================================================
# Deliverable 2 – TinyTroupe Simulation Streamlit App
# =====================================================

st.set_page_config(page_title="TinyTroupe Simulation", page_icon="🎭", layout="centered")

st.title("🎭 TinyTroupe Persona Simulation (Deliverable 2)")
st.markdown(
    """
This app runs AI-driven persona simulations using **TinyTroupe v0.5.2**  
from your Deliverable 1 setup.  
Each persona acts according to defined traits and responds to a discussion topic.  
"""
)

# --- User input fields ---
topic = st.text_area(
    "🗣️ Enter a discussion topic:",
    placeholder="e.g. Evaluate the new productivity app layout.",
    height=100,
)

col1, col2 = st.columns(2)
with col1:
    num_personas = st.number_input("👥 Number of Personas", min_value=2, max_value=6, value=3, step=1)
with col2:
    iterations = st.number_input("🔁 Conversation Rounds", min_value=1, max_value=5, value=2, step=1)

st.markdown("---")

# --- Run simulation button ---
if st.button("▶️ Run Simulation"):
    if not topic.strip():
        st.error("⚠️ Please enter a topic to simulate.")
    else:
        with st.spinner("Simulating personas… this may take a few moments."):
            try:
                transcript = run_simulation(topic, num_personas, iterations)
            except Exception as e:
                st.error(f"❌ Simulation failed: {e}")
                transcript = None

        st.markdown("---")
        st.success("✅ Simulation complete!")
        st.markdown("### 🧠 Conversation Transcript")

        if transcript and isinstance(transcript, str) and len(transcript.strip()) > 0:
            # Display transcript
            st.text_area("Simulation Output", transcript, height=500)

            # Enable file download
            st.download_button(
                "💾 Download Transcript",
                data=transcript.encode("utf-8"),
                file_name="simulation_log.txt",
                mime="text/plain",
            )
        else:
            st.warning("⚠️ No transcript generated. Try a different topic or increase conversation rounds.")

st.markdown("---")
st.caption("TinyTroupe Deliverable 2 • Compatible with academic build v0.5.2 • © 2025 Kaleb Cooper")
