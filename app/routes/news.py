from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import UsefulNews
from app.schemas import NewsResponse, LikeRequest

router = APIRouter(prefix="/news", tags=["News"])


@router.get("/", response_model=list[NewsResponse])
def get_news(
    useful_only: bool | None = Query(default=None),
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    query = db.query(UsefulNews)

    if useful_only is not None:
        query = query.filter(UsefulNews.useful_news == useful_only)

    rows = query.order_by(UsefulNews.published_ts.desc()).limit(limit).all()
    return rows


@router.get("/useful", response_model=list[NewsResponse])
def get_useful_news(
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    rows = (
        db.query(UsefulNews)
        .filter(UsefulNews.useful_news.is_(True))
        .order_by(UsefulNews.published_ts.desc())
        .limit(limit)
        .all()
    )
    return rows


@router.get("/{link:path}", response_model=NewsResponse)
def get_news_by_link(link: str, db: Session = Depends(get_db)):
    row = db.query(UsefulNews).filter(UsefulNews.link == link).first()
    if not row:
        raise HTTPException(status_code=404, detail="News item not found")
    return row


@router.put("/{id}/like")
def update_useful_news(
    id: int,
    payload: LikeRequest,
    db: Session = Depends(get_db)
):

    news = db.query(UsefulNews).filter(UsefulNews.id == id).first()

    if not news:
        raise HTTPException(status_code=404, detail="News not found")

    news.useful_news = payload.useful_news

    db.commit()
    db.refresh(news)

    return {
        "message": "News updated successfully",
        "id": news.id,
        "useful_news": news.useful_news
    }