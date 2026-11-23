from contextlib import asynccontextmanager

from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from app.database import Base, engine
from app.models import ShortUrl  # noqa: F401
from app.rate_limit import limiter
from app.routers import urls


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(lifespan=lifespan, title="URL Shortener", 
            description="A simple URL shortener service", version="1.0.0")

app.include_router(urls.router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)