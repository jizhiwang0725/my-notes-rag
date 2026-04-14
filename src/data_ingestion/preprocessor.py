from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

'''
Chunk one note
'''

def chunkText(text: str, chunkSize: int = 1000, chunckOverlap: int = 200) -> List[str]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunkSize, chunk_overlap=chunckOverlap, separators=["\n\n", "\n", "", ""])
    return splitter.split_text(text)

'''
Chunk all the notes
'''
def chunkAllNotes(notes: List[str]) -> List[List[str]]:
    chunkedNotes = [] 
    for note in notes:
        chunks = chunkText(note)
        chunkedNotes.append(chunks)

    return chunkedNotes

