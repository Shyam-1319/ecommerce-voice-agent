import os
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from groq import APIError, Groq
from pydantic import BaseModel, ConfigDict, Field

load_dotenv(Path(__file__).parent / ".env")

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise RuntimeError("Add GROQ_API_KEY to your .env file.")

client = Groq(
    api_key=api_key,
    timeout=30.0,
    max_retries=0,
)

app = FastAPI(title="E-commerce Voice Support API")


class ChatRequest(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)

    message: str = Field(min_length=1, max_length=2000)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/chat")
def chat(request: ChatRequest):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant. Give concise answers.",
                },
                {
                    "role": "user",
                    "content": request.message,
                },
            ],
            reasoning_effort="low",
            max_completion_tokens=1024,
        )
    except APIError as error:
        raise HTTPException(
            status_code=502,
            detail="The AI provider could not complete the request.",
        ) from error

    answer = response.choices[0].message.content

    if not answer or not answer.strip():
        raise HTTPException(
            status_code=502,
            detail="The AI provider returned an empty answer.",
        )

    return {"answer": answer}