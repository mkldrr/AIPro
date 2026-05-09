import os

from openai import OpenAI


def load_env_file(path: str = ".env") -> None:
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as env_file:
        for line in env_file:
            line = line.strip()

            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def call_llm(
    system_instructions: str,
    user_prompt: str,
    model: str = "gpt-4.1-mini",
) -> str:
    """
    Call a non-reasoning OpenAI model with system instructions and a user prompt.

    Example:
        response = call_llm(
            system_instructions="You are a helpful coding tutor.",
            user_prompt="Explain what a Python function is.",
        )
    """
    load_env_file()
    client = OpenAI()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": user_prompt},
        ],
    )

    return response.choices[0].message.content
