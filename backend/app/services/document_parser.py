import fitz 
#This imports PyMuPDF

#This creates a function called extract_pdf_text. It receives the PDF as raw bytes.
def extract_pdf_text(file_bytes: bytes):
    document = fitz.open(stream=file_bytes, filetype="pdf")#This opens the PDF from memory.

    pages = []#This creates an empty list where we will store the result.

    for page_number, page in enumerate(document, start=1):
        text = page.get_text()

        pages.append({
            "page": page_number,#adds the page number and text into our list
            "text": text
        })

    return pages
#Yes. Overall, this code takes a PDF file, opens it, reads the text from each page, keeps the page number, and returns everything as a list.
def extract_txt_text(file_bytes: bytes):
    text = file_bytes.decode("utf-8")#convert the raw TXT file data into readable text

    return [
        {
            "page": None,
            "text": text
        }
    ]