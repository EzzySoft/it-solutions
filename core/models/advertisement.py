from sqlalchemy import Column, Integer, String

from models.base import Base


class Advertisement(Base):
    __tablename__ = "advertisement"
    ad_id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title: str = Column(String, nullable=False)
    author: str = Column(String, nullable=False)
    views: bytes = Column(Integer, nullable=False)
    position_number = Column(Integer)
