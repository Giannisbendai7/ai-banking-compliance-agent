import requests


def build_context(results):
    context_parts = []

    for result in results:
        context_parts.append(
            f"[Source: {result['source']} | Page: {result['page']}]\n"
            f"{result['text']}"
        )

    return "\n\n".join(context_parts)


def build_prompt(query, context):
    return f"""
You are a banking compliance assistant.

Answer the user's question using only the provided regulatory context.

If the context contains relevant information that partially answers the question, summarize that information and clearly state any limitations. Only say "Insufficient information in the provided regulatory documents." when the context contains no relevant information at all.

Always cite the source and page used for your answer.

User question:
{query}

Regulatory context:
{context}
""".strip()


def ask_llm(query, context):
    prompt = build_prompt(query, context)

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:latest",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]