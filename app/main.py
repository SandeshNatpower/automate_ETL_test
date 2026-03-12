from fastapi import FastAPI
from app.config import settings
from app.routes.news import router as news_router

app = FastAPI(title=settings.APP_NAME)

app.include_router(news_router)


@app.get("/")
def root():
    return {"message": "BBC News API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}

