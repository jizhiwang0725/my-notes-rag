import os 
from typing import List
from langchain.embeddings import HuggingFaceEmbeddings


'''
Create a list of vectors for one chunked note
'''
def createEmbeddings(chunkedNote: List[str]) -> List[List[float]]:
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    return embeddings.embed_documents(chunkedNote)
    

'''
Create a list of vectors for every chunked notes
'''
def createAllEmbeddings(chunkedNotes: List[List[str]]) -> List[List[List[float]]]:
    allEmbeddings = []
    for chunkNote in chunkedNotes:
        allEmbeddings.append(createEmbeddings(chunkNote))
    return allEmbeddings