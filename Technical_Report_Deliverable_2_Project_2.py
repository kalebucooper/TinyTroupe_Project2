
"""

Objective:
------------
This application demonstrates a beta version of a persona-based
simulation framework using the TinyTroupe library (v0.5.2).
It fulfills Deliverable 2 requirements for "Algorithms for
Data Science" by integrating multiple AI-driven personas,
conversation orchestration, and real-time feature evaluation
through a Streamlit UI.


# 1 LIBRARY IMPORTS AND SYSTEM INITIALIZATION


import os
from dotenv import load_dotenv
load_dotenv()

if "OPENAI_API_KEY" not in os.environ or not os.environ["OPENAI_API_KEY"]:
    os.environ["OPENAI_API_KEY"] = "sk-your-real-api-key-here"

import streamlit as st
from simulation_manager import run_simulation

"""
 Algorithmic Rationale:
-------------------------
This architecture separates concerns between:
    (1) the *user interface layer* (Streamlit)
    (2) the *simulation logic* (TinyTroupe orchestrator)
    (3) the *data layer* (persona memory + prompt context)

This modular design mirrors multi-agent frameworks such as
Zhou et al. (2023), “Generative Agents,” and Liang et al. (2024).
"""


# 2 STREAMLIT USER INTERFACE


st.set_page_config(page_title="TinyTroupe Simulation", page_icon="🎭", layout="centered")
st.title("🎭 TinyTroupe Persona Simulation (Deliverable 2)")

st.markdown("""
This app uses **TinyTroupe v0.5.2** to simulate human-like
persona discussions around a given topic. Each persona represents
a unique user archetype with memory, bias, and conversational tone.
""")

topic = st.text_area("🗣️ Discussion Topic", placeholder="e.g. Evaluate the new productivity app layout.", height=100)
col1, col2, col3 = st.columns(3)
with col1:
    num_personas = st.number_input("👥 Personas", min_value=2, max_value=6, value=3)
with col2:
    iterations = st.number_input("🔁 Conversation Rounds", min_value=1, max_value=5, value=2)
with col3:
    api_key = st.text_input("🔑 OpenAI API Key (optional)", type="password")


# 3 RUNNING THE SIMULATION PIPELINE


if st.button("▶️ Run Simulation"):
    if not topic.strip():
        st.error("⚠️ Please enter a discussion topic.")
    else:
        with st.spinner("Simulating personas… please wait..."):
            try:
                transcript = run_simulation(topic, num_personas, iterations)
            except Exception as e:
                st.error(f"❌ Simulation failed: {e}")
                transcript = None

        st.markdown("---")
        st.success("✅ Simulation Complete")
        st.markdown("### 🧠 Conversation Transcript")

        if transcript and isinstance(transcript, str) and len(transcript.strip()) > 0:
            st.text_area("Simulation Output", transcript, height=500)
            st.download_button(
                "💾 Download Transcript",
                data=transcript.encode("utf-8"),
                file_name="simulation_log.txt",
                mime="text/plain",
            )
        else:
            st.warning("⚠️ No transcript generated. Try a different topic or increase rounds.")

st.caption("TinyTroupe Deliverable 2 • © 2025 Kaleb Cooper • Academic Build v0.5.2")
