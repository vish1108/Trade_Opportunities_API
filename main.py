# main.py
from fastapi import FastAPI, Depends, HTTPException, Request
from routers.analyzer import router as analyzer_router
from auth.security import get_current_user, rate_limiter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Trade Opportunities API")

# Middleware (CORS, rate limiting, etc.)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


app.include_router(analyzer_router, prefix="/analyze", tags=["Analyzer"])


@app.get("/")
def root():
    return {"message": "Welcome to the Trade Opportunities API"}
