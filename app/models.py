from sqlalchemy import Column, Text, Date, DateTime, Boolean, BigInteger
from app.database import Base


class UsefulNews(Base):
    __tablename__ = "silver_bbc_useful_news"
    __table_args__ = {"schema": "temporary_data"}

    id = Column(BigInteger, primary_key=True, index=True)

    source_name = Column(Text)
    source_url = Column(Text)
    feed_title = Column(Text)
    extracted_at = Column(Text)

    title = Column(Text)
    link = Column(Text)

    published_raw = Column(Text)
    summary = Column(Text)

    article_id = Column(Text)
    record_source = Column(Text)

    published_ts = Column(DateTime)
    published_date = Column(Date)

    extracted_at_ts = Column(DateTime)
    load_ts = Column(DateTime)
    load_date = Column(Date)

    useful_news = Column(Boolean)