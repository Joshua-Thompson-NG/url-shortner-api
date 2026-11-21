from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse

from app.dependencies import SessionDep
from app.models import ShortUrl
from app.schemas import URLCreate, URLResponse, URLStats
from app.services import create_short_url, get_url_and_increment

router = APIRouter(
    prefix="/urls",
    tags=["urls"],
)

@router.post("/shorten", response_model=URLResponse, status_code=201)
def shorten_url(request: Request, session: SessionDep, url_create: URLCreate):
    url_db = create_short_url(session=session, original_url=url_create.url)
    return {
        "code": url_db.short_code,
        "short_url": f"{request.base_url}urls/{url_db.short_code}",
        "original_url": url_db.original_url,
    }

@router.get("/{code}")
def redirect_to_original(session: SessionDep, code: str):
    url_db = get_url_and_increment(session=session, code=code)
    if not url_db:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return RedirectResponse(url=url_db.original_url)

@router.get("/{code}/stats", response_model=URLStats)
def get_url_stats(session: SessionDep, code: str):
    url_db = session.query(ShortUrl).filter(ShortUrl.short_code == code).first()
    if not url_db:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return url_db
