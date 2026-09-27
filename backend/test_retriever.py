from app.rag.retriever import retrieve_relevant_chunks
chunks = [
    {
        "chunk_index": 0,
        "page": 1,
        "text": "Employees receive 25 paid vacation days every year."
    },
    {
        "chunk_index": 1,
        "page": 2,
        "text": "PostgreSQL is used as the main application database."
    },
    {
        "chunk_index": 2,
        "page": 3,
        "text": "API keys must be stored securely in environment variables."
    }
]
question = "How many vacation days do employees get?"
results=retrieve_relevant_chunks(chunks,question,top_k=2)
for result in results:
    print("Score:", result["score"])
    print("Page:", result["chunk"]["page"])
    print("Text:", result["chunk"]["text"])
    print("-----")