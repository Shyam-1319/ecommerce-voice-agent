import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

# Load the .env file located beside this script.
env_path = Path(__file__).parent / ".env"
load_dotenv(env_path)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("Add GROQ_API_KEY to your .env file.")

client = Groq(api_key=api_key, timeout=30.0)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": "Explain what a voice support agent does in two sentences.",
        }
    ],
    reasoning_effort="low",
    max_completion_tokens=1024,
)

print(response.choices[0].message.content)