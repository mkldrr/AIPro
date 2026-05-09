from openai import OpenAI


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
    client = OpenAI()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_instructions},
            {"role": "user", "content": user_prompt},
        ],
    )

    return response.choices[0].message.content
