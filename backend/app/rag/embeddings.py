from sentence_transformers import SentenceTransformer

model=SentenceTransformer("all-MiniLM-L6-v2")
#Here, model is just a Python variable that stores the embedding model we loaded.In this line:
model = SentenceTransformer("all-MiniLM-L6-v2")
# sentancetransormer loads a pretrained AI model
def generate_embedding(text):
    embedding=model.encode(text)
    #so model.encode text will convert the text into a vector
    return embedding
