import json


def load_chunks(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def search_chunks(chunks, query, top_k=5):
    query_words = query.lower().split()

    scored_chunks = []

    for chunk in chunks:
        text = chunk["text"].lower()

        score = sum(word in text for word in query_words)

        if score > 0:
            scored_chunks.append({
                "source": "EBA Guidelines on ICT and security risk management",
                "page": chunk["page"],
                "text": chunk["text"],
                "score": score
            })

    scored_chunks.sort(key=lambda x: x["score"], reverse=True)

    return scored_chunks[:top_k]