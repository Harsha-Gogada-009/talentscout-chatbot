import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional technical interviewer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=400
    )
    return response.choices[0].message.content.strip()

def technical_questions_prompt(tech_stack: str) -> str:
    return f"""
You are an experienced technical interviewer.

The candidate has declared the following tech stack:
{tech_stack}

Generate 3 to 5 technical interview questions to assess the candidate’s practical knowledge.

Guidelines:
- Focus on real-world usage, not definitions
- One or more questions per technology if possible
- Questions should be concise and clear

Return ONLY the questions as a numbered list.
"""
