from app.services.document_parser import extract_pdf_text
from app.rag.chunker import chunk_pages
from app.rag.retriever import retrieve_relevant_chunks
pdf_path = "../data/rag_chunking_test_document.pdf"
with open(pdf_path, "rb") as file:
    file_bytes = file.read()

pages=extract_pdf_text(file_bytes)
chunks=chunk_pages(pages)


question = "How many vacation days do employees receive?"

results=retrieve_relevant_chunks(chunks,question,top_k=3)

for result in results:
    print("Score:", result["score"])
    print("Page:", result["chunk"]["page"])
    print("Text:", result["chunk"]["text"])
    print("-----")