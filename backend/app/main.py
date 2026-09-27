from fastapi import FastAPI, UploadFile, File, HTTPException

from app.services.document_parser import extract_pdf_text, extract_txt_text
#Go to document_parser.py and bring me the function extract_pdf_text
from app.rag.chunker import chunk_pages
app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/documents/upload")
async def upload_document(file: UploadFile = File(...)):

    allowed_types = ["application/pdf", "text/plain"]

    if file.content_type not in allowed_types:
        raise HTTPException(
            status_code=400,
            detail="Only PDF and TXT files are allowed"
        )

    file_bytes = await file.read()

    if file.content_type == "application/pdf":
        pages = extract_pdf_text(file_bytes)

    elif file.content_type == "text/plain":
        pages = extract_txt_text(file_bytes)
    chunks=chunk_pages(pages)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "chunks": chunks}