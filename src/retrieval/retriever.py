import chromadb
from langchain_huggingface import HuggingFaceEmbeddings
from typing import List, Dict, Any

'''
Function that returns the 5 most similar chunk of text to the query 
'''
def retrieveSimilar(
        query: str,
        topK : int = 5,
        dbPath: str = "data/vector_db", 
        threshold: int = 0.75
) -> List[Dict[str, Any]]:
    client = chromadb.PersistentClient(path=dbPath)
    collection = client.get_collection(name="notes")

    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-l6-v2")
    queryVector = embedder.embed_query(query)

    results = collection.query(
        query_embeddings = [queryVector],
        n_results = topK,
        include=["documents", "metadatas", "distances"]
    )

    chunks = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    return [
        {"text": chunk, "metadata": metadata, "distance": distance} 
        for chunk, metadata, distance in zip(chunks, metadatas, distances) 
        if distance <= threshold
    ]