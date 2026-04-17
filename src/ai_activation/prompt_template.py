from langchain_core.prompts import PromptTemplate

# Template for the prompt feed to the machine
def promptLLM() -> PromptTemplate:
    template = """<|system|>
You are tutor. Your ONLY job is to, using your own word, answer the user's question using the context provided below.
RULES:
1. You must NOT use any outside knowledge.
2. If the answer is not explicitly written in the CONTEXT, you must reply exactly with: "I'm sorry, that information is not in your notes."
3. Do not assume or guess.
============
CONTEXT:
{context}
<|end|>

<|user|>
{question}
<|end|>

<|assistant|>"""

    prompt = PromptTemplate(
        input_variable=["context", "question"],
        template=template
    )

    return prompt