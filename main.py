from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from scrapper import get_gold_rate
import time

cache = {"rate": None, "timestamp": 0}
CACHE_TTL = 10  # seconds

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

BASE_URL = "/api/v1"


@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request: Request, exc: RateLimitExceeded):
    return JSONResponse(
        status_code=429,
        content={"error": "Rate limit exceeded. Try again later."},
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(BASE_URL + "/health")
async def health_check():
    return {"status": "ok"}


@app.get(BASE_URL + "/gold")
@limiter.limit("10/minute")  # 10 requests per minute per IP
async def get_rate(request: Request) -> dict:
    now = time.time()

    if cache["rate"] and (now - cache["timestamp"]) < CACHE_TTL:
        return {"gold_rate": cache["rate"], "cached": True}

    rate = await get_gold_rate()
    if rate is None:
        return {"error": "Failed to fetch gold rate"}

    cache["rate"] = rate
    cache["timestamp"] = now

    return {"gold_rate": rate, "cached": False}
