from .data_ingestion import *
from .vector_store import *
from .retrieval import *
from .generation import *


# Load all the notes 
notes = loadNotesFromFolder("data/notes")

# Chunk all the notes
chunkedNotes = chunkAllNotes(notes)

# Create the vectors for all the chunked notes
allVectors = createAllEmbeddings(chunkedNotes)

# Save the vectors to the database
saveVectors(chunkedNotes=chunkedNotes, vectors=allVectors)

# Ask user for query 
answer = ""
while True:
    query = input("""
==========QUESTION===========
Ask something about your note (press Q to quit)
""").lower()
    
    if query == 'q':
        break
    else: 

        # Find similar texts using cosine similarity function
        similarTexts = retrieveSimilar(query=query, topK=3)
        
        print("===========ANSWER============")

        if not similarTexts:
            print("Sorry, I can not find any notes about this topic. Please try again about other topics!")
        else:
            generateAnswer(myQuestion=query, myNotes=similarTexts) 



# for text in similarTexts:
#     print(text["text"])
#     print(text["metadata"])


