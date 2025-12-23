🤖 TalentScout – AI Hiring Assistant Chatbot
📌 Project Overview

TalentScout is an AI-powered Hiring Assistant chatbot designed to assist recruiters with the initial screening of candidates for technology roles. The chatbot interacts conversationally with candidates, gathers essential personal and professional information, and dynamically generates technical interview questions based on the candidate’s declared tech stack.

This project demonstrates the practical use of Large Language Models (LLMs), prompt engineering, and context-aware conversation handling in a real-world recruitment scenario. TalentScout helps automate early-stage screening while ensuring a structured, fair, and engaging candidate experience.

The application is built using Python and Streamlit and can be run locally or deployed on cloud platforms such as Streamlit Cloud.

✨ Key Features & Capabilities

👋 Automated Greeting & Purpose Explanation

Welcomes candidates and clearly explains the screening process.

🧾 Candidate Information Collection

Collects:

Full Name

Email Address (validated)

Phone Number (validated)

Years of Experience

Desired Position(s)

Current Location

Tech Stack

🧠 Dynamic Technical Question Generation

Generates 3–5 tailored technical questions based on the candidate’s declared tech stack using LLMs.

Example: Python, Django, SQL → Python & backend-related questions.

🗂️ Context-Aware Conversation Flow

Maintains conversation state across multiple steps.

Ensures smooth and coherent interaction.

🛑 Exit & Fallback Handling

Gracefully exits when keywords like exit, bye, or thank you are used.

Provides meaningful prompts for invalid inputs.

🔐 Data Privacy Conscious Design

Candidate data is stored temporarily in-session.

Optional local JSON storage for demonstration purposes only.

🎨 Enhanced Streamlit UI

Clean layout with sidebar progress tracking.

Professional, recruiter-friendly appearance.

🛠️ Installation Instructions (Local Setup)
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/talentscout-chatbot.git
cd talentscout-chatbot

2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # Windows
# OR
source venv/bin/activate  # macOS/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variables

Create a .env file (local only):

OPENAI_API_KEY=your_openai_api_key_here


⚠️ Do NOT commit .env to GitHub.

5️⃣ Run the Application
python -m streamlit run app.py


Open in browser:

http://localhost:8501

▶️ Usage Guide

Launch the Streamlit app.

The chatbot greets the candidate and explains its purpose.

Answer the chatbot’s questions step-by-step.

Provide your tech stack when prompted.

The chatbot generates customized technical questions.

The conversation ends with a confirmation message.

🧩 Technical Details
🔧 Libraries & Tools Used

Python 3.10+

Streamlit – Frontend UI

OpenAI API – Large Language Model

Regex – Input validation

JSON – Lightweight data storage

dotenv – Environment variable handling (local)

🧠 Model Details

Uses OpenAI GPT-based models for:

Natural language understanding

Technical question generation

Temperature and prompts are tuned for clarity and relevance, not creativity.

🏗️ Architecture Overview
Streamlit UI
     ↓
Conversation State (session_state)
     ↓
Prompt Engineering Layer
     ↓
LLM (OpenAI API)
     ↓
Generated Technical Questions

📝 Prompt Design Strategy
Information Gathering Prompts

Designed to be clear, concise, and sequential

Each prompt requests one specific piece of information

Includes validation checks before proceeding

Technical Question Prompts

Dynamically constructed based on tech stack input

Instructs the LLM to:

Generate role-relevant

Skill-specific

Interview-appropriate questions

This ensures the chatbot does not deviate from its intended purpose.

⚠️ Challenges & Solutions
Challenge 1: Maintaining Conversation Context

Solution:
Used Streamlit’s session_state to track conversation stages and candidate data.

Challenge 2: Invalid User Inputs (Email / Phone)

Solution:
Implemented regex-based validation and re-prompting mechanisms.

Challenge 3: Data Privacy & Storage

Solution:

In-memory session storage by default

Optional local JSON storage for demonstration

No sensitive data committed to version control

Challenge 4: Deployment Environment Variables

Solution:

.env file for local development

Streamlit Secrets for cloud deployment

🧹 Code Quality & Structure

Modular code separation (app.py, llm.py, prompts.py)

Clear function names and logical flow

Inline comments for complex logic

Follows Python readability best practices

🗂️ Version Control

Git used for version control

Clear, descriptive commit messages

Public GitHub repository with organized structure

🚀 Deployment
✅ Streamlit Cloud

App deployed using Streamlit Cloud

Environment variables managed via Streamlit Secrets

🔗 Live Demo:
👉 Add your Streamlit Cloud link here

🎥 Demo (Optional but Recommended)

A short video walkthrough demonstrating:

Chatbot interaction

Candidate information collection

Technical question generation

🎬 Demo Link (LOOM):
👉 Add your Loom link here

🔮 Future Enhancements

Sentiment analysis during conversation

Multilingual support

Database-backed persistent storage

Recruiter admin dashboard

Scoring candidate responses

📄 License

This project is developed for educational and evaluation purposes.

✅ Final Note

This project demonstrates LLM integration, prompt engineering, UI design, and deployment readiness, making it a strong submission for an AI/ML Intern role.