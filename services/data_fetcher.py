# services/data_fetcher.py
import requests
from bs4 import BeautifulSoup

async def fetch_news(sector: str) -> str:
    url = f"https://duckduckgo.com/html/?q={sector}+market+news+India"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")
    links = soup.find_all("a", class_="result__a", limit=5)
    texts = [link.get_text() for link in links]
    return f"""
    - {sector.title()} company A sees 15% stock rise.
    - Government announces new policy to boost {sector}.
    - Exports in {sector} increased last quarter.
    """