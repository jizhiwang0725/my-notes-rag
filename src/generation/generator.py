from .phi_activation import ragChain
from typing import List, Any, Dict
from src.utils import timer

'''
Generates well structured answer 
'''
@timer
def generateAnswer(myQuestion: str, myNotes: List[Dict[str, Any]]):

    # Notes used for the prompt 
    myNotes = "\n\n".join(text["text"] for text in myNotes)
    notes = f"""==============NOTES=============
{myNotes}
================================"""
    print(notes)
   
    print("THINKING...")
    
    response = ragChain.stream({
        "context": myNotes,
        "question": myQuestion
    })

    for chunk in response:
    # print the chunk immediately without a new line
        print(chunk, end="", flush=True)