from sentence_transformers import util
from app.rag.embeddings import generate_embedding
text1 = "I like cats"
text2 = "I love kittens"
text3 = "PostgreSQL stores application data"
embedding1 = generate_embedding(text1)
embedding2 = generate_embedding(text2)
embedding3 = generate_embedding(text3)
similarity_1_2 = util.cos_sim(embedding1, embedding2)
similarity_1_3 = util.cos_sim(embedding1, embedding3)
print("Cats vs kittens:", similarity_1_2)
print("Cats vs PostgreSQL:", similarity_1_3)

