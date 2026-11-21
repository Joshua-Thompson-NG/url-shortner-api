from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class URLCreate(BaseModel):
    url: HttpUrl = Field(..., description="The URL to be shortened")

class URLResponse(BaseModel):
    code: str = Field(..., description="The shortened URL code")
    short_url: HttpUrl = Field(..., description="The full shortened URL")
    original_url: HttpUrl = Field(..., description="The original URL")

    model_config = ConfigDict(from_attributes=True)


class URLStats(BaseModel):
    short_code: str = Field(..., description="The shortened URL code")
    original_url: HttpUrl = Field(..., description="The original URL")
    clicks: int = Field(..., 
                description="The number of times the shortened URL has been accessed")
    created_at: datetime = Field(..., 
                description="The date and time when the shortened URL was created")

    model_config = ConfigDict(from_attributes=True)
    