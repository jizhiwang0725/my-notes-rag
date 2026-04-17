from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
import torch

# Model, instruct tuned - explicitly built to answer questions rather than just autocompleting text
model_id = "microsoft/Phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.float16,
    attn_implementation="sdpa"
)

model = model.to("mps")

pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    truncation=True,
    max_length=3500,
    max_new_tokens=500,
    do_sample=True,
    temperature=0.1,
    top_p=0.95,
    repetition_penalty=1.05,
    no_repeat_ngram_size=3,
    return_full_text=False
)

llm = HuggingFacePipeline(pipeline=pipe)

# Template for the prompt feed to the machine
template = """<|system|>
You are a factual AI tutor. Answer the user's question using ONLY the provided notes.
If the answer is not in the context, say "I don't know". Do not repeat sentences 
====
Notes:
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

# The "|" symbol tells LangChain ot send the output of the prompt directly into the LLM 
ragChain = prompt | llm

print("AI engine activated!")