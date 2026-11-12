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



messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant. Give clear, concise answers.",
    }
]

print("chat started. Type 'exit' to finish.")

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        print("Chat ended.")
        break

    if not question:
        print("Please enter a question.")
        continue

    messages.append({
        "role": "user",
        "content": question,
    })

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        reasoning_effort="low",
        max_completion_tokens=1024,
    )


    answer = response.choices[0].message.content
    print(f"\nAssistant: {answer}")

    messages.append({
        "role": "assistant",
        "content": answer,
    })