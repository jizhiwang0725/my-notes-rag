import chromadb 
from chromadb.config import Settings 
from typing import List, Dict, Any


'''
Clears the database
'''
def clearDatabase(dbPath: str = "data/vector_db"):
    import shutil, os
    if os.path.exists(dbPath):
        shutil.rmtree(dbPath)

'''
Store every vectors and its corrisponding chunk for all notes
'''
def saveVectors(chunkedNotes: List[List[str]], vectors: List[List[List[float]]], dbPath: str = "data/vector_db"):
    clearDatabase(dbPath=dbPath)
    client = chromadb.PersistentClient(path=dbPath)

    collection = client.create_collection(
        name="notes",
        metadata={"hnsw:space": "cosine"})

    for noteNum in range(len(chunkedNotes)):

        
        chunkedNote = chunkedNotes[noteNum]
        numOfChunks = len(chunkedNote)
        noteVectors = vectors[noteNum]

        ids = [f"chunk_{noteNum}_{index}" for index in range(numOfChunks)]
        documents = chunkedNote
        metadatas = [{"noteNum": noteNum+1, "chunkIndex": i+1} for i in range(numOfChunks)]

        collection.add(
            embeddings=noteVectors,
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

