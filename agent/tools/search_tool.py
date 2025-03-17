import requests
from config import GOOGLE_API_KEY,CX_KEY

def search_google(query):
    """Performs a Google search."""
    url = f"https://www.googleapis.com/customsearch/v1?key={GOOGLE_API_KEY}&cx={CX_KEY}&q={query}" #Replace YOUR_CX with your custom search engine ID
    try:
        response = requests.get(url)
        response.raise_for_status()
        results = response.json().get("items", [])
        return [result["snippet"] for result in results]
    except requests.exceptions.RequestException as e:
        return f"Search failed: {e}"