from sqlalchemy import Column, Integer, String, LargeBinary

from models.base import Base


class User(Base):
    __tablename__ = "user"
    user_id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username: str = Column(String, nullable=False, unique=True)
    email: str = Column(String, nullable=False, unique=True)
    password_hash: bytes = Column(LargeBinary)
