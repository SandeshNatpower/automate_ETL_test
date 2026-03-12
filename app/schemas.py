from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel


class NewsResponse(BaseModel):
    title: Optional[str]
    link: str
    summary: Optional[str]
    published_ts: Optional[datetime]
    published_date: Optional[date]
    source_name: Optional[str]
    useful_news: Optional[bool]

    class Config:
        from_attributes = True


class LikeRequest(BaseModel):
    useful_news: bool