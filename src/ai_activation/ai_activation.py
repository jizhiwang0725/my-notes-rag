from .prompt_template import promptLLM
from .phi_activation import phiActivate
from .ollama_phi_activation import ollamaPhiActivate

def aiActivate():
    prompt = promptLLM()
    llm = phiActivate()

    # The "|" symbol tells LangChain ot send the output of the prompt directly into the LLM 
    ragChain = prompt | llm

    print("AI engine activated!")

    return ragChain 