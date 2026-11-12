# E-commerce Voice Support Agent

A portfolio project building toward voice-based customer support
for a fictional online store.

## Current implementation

The current prototype is a terminal chatbot using Groq's API.

- Accepts questions entered in the terminal.
- Generates responses using the openai/gpt-oss-20b model.
- Sends conversation history with each request.
- Remembers earlier messages during the running session.
- Skips empty input and exits when the user types `exit`.
- Loads the API key from a local `.env` file.

Conversation history is held in memory and resets when the program restarts.

## Planned capabilities

- Browser-based voice conversations.
- Order status lookup.
- Answers grounded in delivery and return policies.
- Return requests with customer confirmation.
- Human support escalation.

## Fresh setup on Windows

Prerequisites are Python 3.13, Git, and a Groq API key.

Clone the repository and enter its folder.

```powershell
git clone https://github.com/Shyam-1319/ecommerce-voice-agent.git
cd ecommerce-voice-agent
```

Create a virtual environment and install dependencies.

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Create a `.env` file from the template.

```powershell
Copy-Item .env.example .env
```

Open `.env` and enter your key after `GROQ_API_KEY=`.
Keep your actual key private.

## Run the chatbot

```powershell
.\.venv\Scripts\python.exe first_request.py
```

Enter a message at the `You:` prompt. Type `exit` to finish.

## Limitations

- Conversation history grows with each exchange, increasing token usage.
- API and network errors currently stop the program.
- Customer support tools and voice features are planned.