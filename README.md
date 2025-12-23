# 🤖 TalentScout – AI Hiring Assistant Chatbot

## 📌 Project Overview

TalentScout is an **AI-powered Hiring Assistant chatbot** designed to assist recruiters with the **initial screening of candidates** for technology roles. The chatbot interacts conversationally with candidates, gathers essential personal and professional information, and dynamically generates **technical interview questions** based on the candidate’s declared tech stack.

This project demonstrates the practical use of **Large Language Models (LLMs)**, **prompt engineering**, and **context-aware conversation handling** in a real-world recruitment scenario. TalentScout helps automate early-stage screening while ensuring a structured, fair, and engaging candidate experience.

The application is built using **Python and Streamlit** and can be run locally or deployed on cloud platforms such as **Streamlit Cloud**.

---

## ✨ Key Features & Capabilities
- **Live Link for the project** - https://talentscout-chatbot-du9gmhmbbfkr5fss4n3g4p.streamlit.app/
- 👋 **Automated Greeting & Purpose Explanation**
  - Welcomes candidates and clearly explains the screening process.

- 🧾 **Candidate Information Collection**
  - Collects:
    - Full Name  
    - Email Address (validated)  
    - Phone Number (validated)  
    - Years of Experience  
    - Desired Position(s)  
    - Current Location  
    - Tech Stack  

- 🧠 **Dynamic Technical Question Generation**
  - Generates **3–5 tailored technical questions** based on the candidate’s declared tech stack using LLMs.

- 🗂️ **Context-Aware Conversation Flow**
  - Maintains conversation state across multiple steps for coherent interaction.

- 🛑 **Exit & Fallback Handling**
  - Gracefully exits when keywords like `exit`, `bye`, or `thank you` are used.
  - Provides meaningful prompts for invalid inputs.

- 🔐 **Data Privacy Conscious Design**
  - Candidate data is stored in-memory by default.
  - Optional local JSON storage for demonstration purposes only.

- 🎨 **Enhanced Streamlit UI**
  - Clean layout with sidebar progress tracking.
  - Professional, recruiter-friendly interface.

---

## 🛠️ Installation Instructions (Local Setup)

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/talentscout-chatbot.git
cd talentscout-chatbot
