import json


def chunk_pages(pages, chunk_size=1000, overlap=200):
    chunks = []

    for page in pages:
        text = page["text"]

        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append({
                "page": page["page"],
                "text": chunk_text
            })

            if end >= len(text):
                break

            start = end - overlap

    return chunks


def save_chunks(chunks, output_path):
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(chunks, file, ensure_ascii=False, indent=2)