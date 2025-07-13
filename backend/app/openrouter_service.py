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

        if not search_results:
            return "Aucun résultat web trouvé."

        sources = "\n\n".join([
            f"[{i+1}] {r['title']} ({r['href']})\n{r['body']}"
            for i, r in enumerate(search_results)
        ])

        full_prompt = f"""Tu es un assistant doté d'une capacité à lire et interpréter des résultats de recherche web.

Voici des informations extraites de recherches récentes :

{sources}

En te basant uniquement sur ces résultats, réponds à la question suivante de manière claire, synthétique et avec un ton professionnel :

"{prompt}"

Si les informations ci-dessus sont insuffisantes pour répondre, indique-le."""
        
        response = openai.ChatCompletion.create(
            model="qwen/qwq-32b:free",
            messages=[
                {"role": "system", "content": "Tu es un assistant expert en IA générative, capable de répondre avec clarté en te basant sur des sources web fournies."},
                {"role": "user", "content": full_prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Erreur lors de l'appel à OpenRouter : {e}"