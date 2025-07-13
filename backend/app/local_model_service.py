from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
from app.web_search import search_web

model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float32)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def ask_local_model(prompt: str) -> str:
    try:
        search_results = search_web(prompt, max_results=3)
        search_summary = "\n".join([
            f"[{i+1}] {r['title']} - {r['href']}\n{r['body']}"
            for i, r in enumerate(search_results)
        ])

        full_prompt = f"""Voici des informations trouvées en ligne :

{search_summary}

À partir de ces sources, réponds à la question suivante de manière synthétique et précise :
{prompt}
"""

        output = generator(full_prompt, max_new_tokens=300, do_sample=True, temperature=0.7)
        return output[0]["generated_text"]
    except Exception as e:
        return f"Erreur dans le modèle local : {e}"
