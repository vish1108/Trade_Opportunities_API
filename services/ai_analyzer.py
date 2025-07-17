import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
#GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"

async def analyze_with_gemini(sector: str, news_text: str) -> str:
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{
            "parts": [{
                "text": f"Analyze recent news for the {sector} sector in India and summarize trade opportunities.\\n\\n{news_text}"
            }]
        }]
    }

    response = requests.post(f"{GEMINI_URL}?key={GEMINI_API_KEY}", headers=headers, data=json.dumps(payload))
    # print("response.status_code:", response.status_code)
    # print("response text:", response.text)


    if response.status_code != 200:
        return "LLM analysis failed."
    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
