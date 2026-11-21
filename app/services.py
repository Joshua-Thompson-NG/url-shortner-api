import secrets
import string

from pydantic import HttpUrl

from app.dependencies import SessionDep
from app.models import ShortUrl


def generate_code(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(secrets.choice(chars) for _ in range(length))

def create_short_url(session: SessionDep, original_url: HttpUrl):
    code = generate_code()
    url_db = ShortUrl(short_code=code, original_url=str(original_url))
    session.add(url_db)
    session.commit()
    session.refresh(url_db)
    return url_db

def get_url_and_increment(session: SessionDep, code: str):
    url_db = session.query(ShortUrl).filter(ShortUrl.short_code == code).first()
    if url_db:
        url_db.clicks += 1
        session.commit()
        session.refresh(url_db)
    return url_db