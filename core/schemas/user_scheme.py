from typing import Optional
from pydantic import BaseModel, EmailStr


class CredentialsScheme(BaseModel):
    login: str
    password: str


class CreateUserScheme(BaseModel):
    email: EmailStr
    username: str
    password: str = None


class UserScheme(BaseModel):
    user_id: int
    email: EmailStr
    username: str
    password_hash: Optional[bytes] = None
