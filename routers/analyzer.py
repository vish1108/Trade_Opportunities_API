from fastapi import APIRouter, HTTPException, Depends
from services.data_fetcher import fetch_news
from services.ai_analyzer import analyze_with_gemini
from services.markdown_generator import generate_markdown
from auth.security import get_current_user
from fastapi.responses import PlainTextResponse 
from fastapi import Security
from fastapi.security import HTTPAuthorizationCredentials
from auth.security import security, get_current_user

router = APIRouter()


@router.get("/{sector}")
async def analyze_sector(
    sector: str,
    credentials: HTTPAuthorizationCredentials = Security(security),  # This enables Swagger auth box
    user: str = Depends(get_current_user)
):
    
    # print(f"[DEBUG] Authenticated request by user: {user}")
    # print(f"[DEBUG] Sector received: {sector}")
    if not sector.isalpha():
        print("[DEBUG] Invalid sector name.")
        raise HTTPException(status_code=400, detail="Invalid sector name.")

    news = await fetch_news(sector)
    if not news:
        print("[DEBUG] No news found for sector.")
        raise HTTPException(status_code=404, detail="No news found for this sector.")

    summary = await analyze_with_gemini(sector, news)
    markdown = generate_markdown(sector, news, summary)
    #print("[DEBUG] Successfully generated markdown report.")
    #return {"report": markdown}
    return markdown

