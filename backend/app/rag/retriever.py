from sentence_transformers import util
from app.rag.embeddings import generate_embedding


def retrieve_relevant_chunks(chunks, question, top_k=3):
    question_embedding = generate_embedding(question)

    scored_chunks = []

    for chunk in chunks:
        chunk_embedding = generate_embedding(chunk["text"])

        similarity = util.cos_sim( question_embedding,chunk_embedding)
        score=similarity.item()
        scored_chunks.append({
            "chunk": chunk,
            "score": score
        })
    scored_chunks.sort(key=lambda item : item["score"],reverse=True)
    #For every item in scored_chunks, look at its score, and use that score to decide the sorting order.
    return scored_chunks[:top_k]