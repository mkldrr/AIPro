# AGENTS.md

## Project Goal

This project is for learning how to use LLMs effectively and for building an AI agent step by step over the next few weeks.

## Current Stage

- Focus on learning model usage, prompting, and agent design.
- Keep the implementation simple and easy to understand.
- Start with Python helper functions before building a full app.
- Do not build UI pages, HTML, CSS, or frontend files unless explicitly requested.

## Working Rules

- Wait for clear instructions before creating new features or files.
- Explain important changes briefly.
- Keep code beginner-friendly and readable.
- Do not hardcode API keys or secrets.
- Use `.env` for local secrets such as `OPENAI_API_KEY`.
- Do not print or expose secret values.
- Prefer small, focused commits.

## Project Commands

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Check Python syntax:

```bash
python3 -m py_compile llm.py
```

## Current Files

- `llm.py`: helper for calling a non-reasoning OpenAI chat model.
- `requirements.txt`: Python dependencies.
- `.env`: local secrets file, ignored by git.

## Agent Direction

The future app may include:

- A model calling layer
- System instructions
- User prompts
- Model parameters
- Tools
- Memory
- Planning
- A simple app interface when the project is ready for UI work
