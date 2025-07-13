import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENROUTER_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

def ask_openrouter(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="qwen/qwen-2.5-32b-instruct",
            messages=[
                {"role": "system", "content": "Tu es un assistant utile."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Erreur lors de l'appel à OpenRouter : {e}"
