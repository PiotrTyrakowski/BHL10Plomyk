from pydantic import BaseModel, Field
from typing import List, Optional

class CertificateBase(BaseModel):
    name: str

class UserBase(BaseModel):
    username: str
    bio: Optional[str] = None
    contact: Optional[str] = None

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: str
    certificates: List[CertificateBase] = []

    class Config:
        orm_mode = True

