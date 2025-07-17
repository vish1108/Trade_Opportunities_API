
import time
from collections import defaultdict
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.status import HTTP_401_UNAUTHORIZED
import time
from collections import defaultdict

# Fake user token mapping
TOKENS = {"test-token": "test-user"}

# Rate limit per IP
RATE_LIMITS = defaultdict(lambda: [0, 0])

# Set up HTTP Bearer scheme for Swagger UI
security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    print(f"[DEBUG] Received token: {token}")  # Print the token
    if token not in TOKENS:
        print("[DEBUG] Token not found in TOKENS list.")
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid token")
    print("[DEBUG] Token is valid. User:", TOKENS[token])
    return TOKENS[token]

async def rate_limiter(request):
    ip = request.client.host
    now = int(time.time())
    window, count = RATE_LIMITS[ip]
    if now - window > 60:
        RATE_LIMITS[ip] = [now, 1]
    elif count >= 10:
        raise HTTPException(status_code=429, detail="Too many requests")
    else:
        RATE_LIMITS[ip][1] += 1
