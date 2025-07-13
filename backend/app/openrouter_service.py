from dotenv import load_dotenv
import os
import openai
from app.web_search import search_web


load_dotenv()

openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def ask_openrouter(prompt: str) -> str:
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

        response = openai.ChatCompletion.create(
            model="qwen/qwen2.5-vl-32b-instruct:free",
            messages=[
                {"role": "system", "content": "Tu es un assistant intelligent avec accès web."},
                {"role": "user", "content": full_prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Erreur : {e}"