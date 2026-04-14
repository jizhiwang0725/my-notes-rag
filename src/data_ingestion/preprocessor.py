from langchain.text_splitter import RecursiveCharacterTextSplitter

"""
Chunking one file
"""
def chunkText(text: str, chunkSize: int = 1000, chunckOverlap: int = 200) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunkSize, chunk_overlap=chunckOverlap, separators=["\n\n", "\n", "", ""])
    return splitter.split_text(text)

def chunkAllNotes(notes: list[str]) -> list[list[str]]:
    chunkedNotes = [] 
    for note in notes:
        chunks = chunkText(note)
        chunkedNotes.append(chunks)

    return chunkedNotes

