from app.rag.chunker import chunk_pages


pages = [
    {
        "page": 1,
        "text": "I am learning how RAG applications work with Python today"
    }
]

chunks = chunk_pages(pages,chunk_size=5,overlap=2)


print(chunks)