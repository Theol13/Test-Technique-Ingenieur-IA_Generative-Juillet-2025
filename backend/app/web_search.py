from duckduckgo_search import DDGS

def search_web(query: str, max_results: int = 3) -> list:
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=max_results)
        return [{"title": r["title"], "href": r["href"], "body": r["body"]} for r in results]