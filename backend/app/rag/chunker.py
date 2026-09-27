def chunk_pages(pages,chunk_size=200,overlap=50):
    #list where we are gonna store ou chunks
    chunks=[]
     #So inside chunk_pages, we want Python to take page 1, process it, 
     # then page 2, and so on.
     #  That is what a for loop does.
    for page in pages:
       
        words=page["text"].split()
        start =0
        chunk_index=0
        #every time while loop creates new chunk
        while start < len(words):
            remaining_words=len(words)-start
            if remaining_words<=overlap:
                break
            end = start + chunk_size
            chunk_words = words[start:end]
            #joining the chunk words
            chunk_text=" ".join(chunk_words)
            #adding  this dict into chunks list
            chunks.append({
                "chunk_index":chunk_index,
                "page":page["page"],
                "text":chunk_text

            })
            chunk_index = chunk_index+1
            start+=chunk_size-overlap
    return chunks
