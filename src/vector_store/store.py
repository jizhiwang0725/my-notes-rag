import chromadb 
from chromadb.config import Settings 
from typing import List, Dict, Any


'''
Store every vectors and its corrisponding chunk for all notes
'''
def saveVectors(chunkedNotes: List[List[str]], vectors: List[List[List[float]]], dbPath: str = "data/vector_db"):
    client = chromadb.PersistentClient(path=dbPath)
    collection = client.get_or_create_collection(name="notes")

    for noteNum in range(len(chunkedNotes)):

        
        chunkedNote = chunkedNotes[noteNum]
        numOfChunks = len(chunkedNote)
        noteVectors = vectors[noteNum]

        ids = [f"chunk_{noteNum}_{index}" for index in range(numOfChunks)]
        documents = chunkedNote
        metadatas = [{"noteNum": noteNum, "chunkIndex": i} for i in range(numOfChunks)]

        collection.add(
            embeddings=noteVectors,
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

