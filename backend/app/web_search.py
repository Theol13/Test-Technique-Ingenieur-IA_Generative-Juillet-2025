import os
from serpapi import GoogleSearch
from dotenv import load_dotenv

load_dotenv()

def search_web(prompt: str, max_results: int = 3) -> list:
    params = {
        "q": prompt,
        "api_key": os.getenv("SERPAPI_KEY"),
        "num": max_results,
        "hl": "fr"
    }

    try:
        search = GoogleSearch(params)
        results = search.get_dict().get("organic_results", [])
        
        return [
            {
                "title": r.get("title"),
                "href": r.get("link"),
                "body": r.get("snippet", "")
            }
            for r in results[:max_results]
        ]
    except Exception as e:
        print("Erreur SerpAPI :", e)
        return []
