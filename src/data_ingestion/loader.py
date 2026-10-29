import os
from pypdf import PdfReader
from typing import List
import re


'''
Load a single file 
'''
def loadFile(filePath: str) -> str:
    if not os.path.exists(filePath):
        raise FileNotFoundError(f"File not found: {filePath}")

    ext = os.path.splitext(filePath)[1].lower()
    if ext == ".txt":
        return loadTextFile(filePath)
    if ext == ".pdf":
        return loadPdfFile(filePath)

    raise ValueError(f"Unsupported file type: {ext}. Supported: .txt, .pdf")

'''
Helper functions for different file types (pdf/txt)
'''
def loadTextFile(filePath: str) -> str:
    with open(filePath, 'r') as file:
        return file.read()
    
def loadPdfFile(filePath: str) -> str:
    reader = PdfReader(filePath)
    pages = []
    for page in reader.pages:
        pageText = page.extract_text()
        if pageText:
            pages.append(pageText)
    return "\n".join(pages)

'''
Load all the files in the folder 
'''
def loadNotesFromFolder(folderPath: str) -> List[str]:
    notes = []
    for fileName in os.listdir(folderPath):
        filePath = os.path.join(folderPath, fileName)
        
        if not os.path.isfile(filePath):
            continue

        try:
            content = loadFile(filePath)
            notes.append(content)
        
        except (FileNotFoundError, ValueError) as error:
            print(f"Skipped {fileName}: {error}")

    return cleanFile(notes)

'''
Clean all the files 
'''
def cleanFile (rawTexts: List[str]) -> List[str]:
    cleanTexts = []
    for rawText in rawTexts:
        
        # This looks for lines that only contain bullets, spaces, or tabs, and deletes them
        cleanText = re.sub(r'^[•\s]+$', '', rawText, flags=re.MULTILINE)

        # Clean up any massive empty gaps left behind
        cleanText = re.sub(r'\n{2,}', '\n\n', cleanText)
        cleanText = re.sub(r'^—+$', '\n\n', cleanText)
        cleanText = re.sub(r'[\n\t\r]+', ' ', cleanText)
        
        
        cleanTexts.append(cleanText)
    
    return cleanTexts 


