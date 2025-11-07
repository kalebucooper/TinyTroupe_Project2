# 🎭 TinyTroupe Persona Simulation (Deliverable 2)

**Course:** Algorithms for Data Science  
**Student:** Kaleb Cooper  
**Date:** November 7, 2025  
**Instructor:** Prof. Kaleemunnisa  

---

## 🧠 Project Overview

This project implements **Deliverable 2** of the *TinyTroupe Persona Simulation* system, a Streamlit-based beta application built for the Algorithms for Data Science course.

The app uses the **TinyTroupe v0.5.2** package to simulate AI-driven personas that discuss and evaluate a product feature (e.g., “Evaluate the new productivity app”).  
Each persona represents a distinct user type with individual perspectives and communication styles.  

Deliverable 2 focuses on:
- Developing a **functional, user-friendly simulation interface**.
- Enabling **multi-persona discussions** with dynamic topic input.
- Generating **meaningful, natural-language feedback**.
- Demonstrating **end-to-end deployment readiness** for instructor testing.

---

## 🚀 How to Run the App

### 1. Clone the Repository
```bash
git clone https://github.com/kalebucooper/TinyTroupe_Project2.git
cd TinyTroupe_Project2
```

### 2. Set Up the Environment
Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate   # On macOS/Linux
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
Create a `.env` file in the same directory as `app.py`:
```
OPENAI_API_KEY=sk-your-real-api-key-here
```

### 5. Run the App
```bash
streamlit run app.py
```

Then open the local URL (default: [http://localhost:8501](http://localhost:8501)) in your browser.

---

## 🧩 File Descriptions

| File | Description |
|------|--------------|
| **app.py** | Main Streamlit interface for running persona simulations. |
| **simulation_manager.py** | Core simulation logic that manages TinyTroupe personas and generates transcripts. |
| **requirements.txt** | Lists all Python dependencies needed to run the app. |
| **Technical_Report_Deliverable_2_Project_2.py** | Annotated technical report explaining design choices, algorithm flow, and improvements. |
| **.env** | Local API key file (⚠️ *Do not upload to GitHub*). |

---

## 🧪 Simulation Capabilities

- Multi-agent persona conversations using TinyTroupe v0.5.2.  
- Customizable input fields:
  - Topic  
  - Number of personas (2–6)  
  - Conversation rounds (1–5)  
- Real-time transcript display.  
- Downloadable output (`simulation_log.txt`).  
- Fully local and reproducible (no external database required).

---

## 🧱 Technical Notes

- Built with **Streamlit**, **TinyTroupe**, and **OpenAI GPT-4.1-mini** backend.  
- Auto-loads API key from `.env` (via `dotenv`).  
- Designed for local or cloud deployment (Hugging Face Spaces compatible).  
- Modular architecture for easy integration of additional personas or conversation logic.

---

## 📜 Academic Context

This submission fulfills **Deliverable 2: Beta Version and Technical Report**, demonstrating:
- A working prototype of a persona-based simulation app.
- Integration of user interface, algorithmic design, and conversation generation.
- Alignment with the project’s research objectives for dynamic persona evaluation.

---

## 🧑‍💻 Author
**Kaleb Cooper**  
Department of Computer Science  
Pace University — Seidenberg School  
© 2025
