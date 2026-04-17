from langchain_community.llms import Ollama 

def ollamaPhiActivate() -> Ollama:
    return Ollama(model="phi3", num_ctx=4096)