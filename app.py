import streamlit as st
import re
import json
from datetime import datetime

from llm import generate_response
from prompts import technical_questions_prompt

# -----------------------------
# Persist Candidate Data
# -----------------------------
def save_candidate(candidate: dict):
    record = {
        **candidate,
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        with open("candidates.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(record)

    with open("candidates.json", "w") as f:
        json.dump(data, f, indent=2)

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Custom CSS (Safe for Streamlit Cloud)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #f9fafb;
}

.header-box {
    background: white;
    padding: 1.5rem;
    border-radius: 14px;
    border: 1px solid #e5e7eb;
    margin-bottom: 1.5rem;
}

.chat-note {
    color: #6b7280;
    font-size: 0.9rem;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="header-box">
    <h2>🤖 TalentScout Hiring Assistant</h2>
    <p class="chat-note">
        AI-powered chatbot for initial candidate screening and technical assessment
    </p>
</div>
""", unsafe_allow_html=True)

EXIT_KEYWORDS = ["exit", "quit", "bye", "thank you", "thanks"]

# -----------------------------
# Validators
# -----------------------------
def is_valid_email(email: str) -> bool:
    return re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email) is not None

def is_valid_phone(phone: str) -> bool:
    return re.match(r"^\d{10,15}$", phone) is not None

def is_valid_experience(exp: str) -> bool:
    try:
        return float(exp) >= 0
    except ValueError:
        return False

# -----------------------------
# Initialize Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "stage" not in st.session_state:
    st.session_state.stage = "name"

if "candidate" not in st.session_state:
    st.session_state.candidate = {
        "name": "",
        "email": "",
        "phone": "",
        "experience": "",
        "position": "",
        "location": "",
        "tech_stack": ""
    }

# -----------------------------
# Sidebar (Progress + Info)
# -----------------------------
with st.sidebar:
    st.markdown("### 📋 Screening Progress")
    st.write(f"**Current Stage:** {st.session_state.stage.capitalize()}")

    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.write(
        "TalentScout uses AI to assist recruiters with "
        "initial candidate screening in a structured and fair way."
    )

# -----------------------------
# Stage Prompts
# -----------------------------
stage_prompts = {
    "email": "Thanks! What is your **email address**?",
    "phone": "Please share your **phone number** (10–15 digits).",
    "experience": "How many **years of experience** do you have?",
    "position": "What **position(s)** are you applying for?",
    "location": "Where is your **current location**?",
    "tech_stack": (
        "Please list your **tech stack**.\n\n"
        "Include programming languages, frameworks, databases, and tools."
    )
}

# -----------------------------
# Initial Greeting (ONCE)
# -----------------------------
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({
        "role": "assistant",
        "content": (
            "Hello! 👋 Welcome to **TalentScout**, your AI-powered hiring assistant.\n\n"
            "I’ll help with the **initial screening process** by collecting a few details "
            "and then asking **technical questions based on your tech stack**.\n\n"
            "👉 What is your **full name**?"
        )
    })

# -----------------------------
# Display Chat History
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(msg["content"])

# -----------------------------
# User Input
# -----------------------------
user_input = st.chat_input("Type your answer here...")

if user_input:

    # Exit handling
    if any(k in user_input.lower() for k in EXIT_KEYWORDS):
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({
            "role": "assistant",
            "content": (
                "🙏 Thank you for your time!\n\n"
                "Your information has been recorded successfully.\n"
                "Our recruitment team will reach out if your profile matches.\n\n"
                "Have a great day!"
            )
        })
        st.session_state.stage = "completed"
        st.rerun()

    if st.session_state.stage == "completed":
        st.session_state.messages.append({
            "role": "assistant",
            "content": "✅ This conversation has already been completed."
        })
        st.rerun()

    st.session_state.messages.append({"role": "user", "content": user_input})

    # -----------------------------
    # Conversation Flow
    # -----------------------------
    if st.session_state.stage == "name":
        st.session_state.candidate["name"] = user_input
        st.session_state.stage = "email"
        reply = stage_prompts["email"]

    elif st.session_state.stage == "email":
        if not is_valid_email(user_input):
            reply = "⚠️ Please enter a valid email address (e.g., name@gmail.com)."
        else:
            st.session_state.candidate["email"] = user_input
            st.session_state.stage = "phone"
            reply = stage_prompts["phone"]

    elif st.session_state.stage == "phone":
        if not is_valid_phone(user_input):
            reply = "⚠️ Please enter a valid phone number (digits only)."
        else:
            st.session_state.candidate["phone"] = user_input
            st.session_state.stage = "experience"
            reply = stage_prompts["experience"]

    elif st.session_state.stage == "experience":
        if not is_valid_experience(user_input):
            reply = "⚠️ Please enter experience as a number (e.g., 2 or 3.5)."
        else:
            st.session_state.candidate["experience"] = user_input
            st.session_state.stage = "position"
            reply = stage_prompts["position"]

    elif st.session_state.stage == "position":
        st.session_state.candidate["position"] = user_input
        st.session_state.stage = "location"
        reply = stage_prompts["location"]

    elif st.session_state.stage == "location":
        st.session_state.candidate["location"] = user_input
        st.session_state.stage = "tech_stack"
        reply = stage_prompts["tech_stack"]

    elif st.session_state.stage == "tech_stack":
        st.session_state.candidate["tech_stack"] = user_input

        with st.spinner("Generating technical questions..."):
            prompt = technical_questions_prompt(user_input)
            questions = generate_response(prompt)

        save_candidate(st.session_state.candidate)

        reply = (
            "🧠 **Technical Questions Based on Your Tech Stack:**\n\n"
            f"{questions}\n\n"
            "✅ Thank you for completing the initial screening!\n"
            "Our recruitment team will contact you with next steps."
        )

        st.session_state.stage = "completed"

    else:
        reply = "Thank you."

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
