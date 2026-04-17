from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig
from langchain_huggingface import HuggingFacePipeline
import torch

'''
Activatie microsoft Phi-3 instructive tuned model with 4k tokens limit 
'''
def phiActivate() -> HuggingFacePipeline:
    
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

    return HuggingFacePipeline(pipeline=pipe) 

