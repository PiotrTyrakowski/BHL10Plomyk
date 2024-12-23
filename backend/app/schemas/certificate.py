from pydantic import BaseModel
from typing import Optional

class CertificateBase(BaseModel):
    name: str

class CertificateCreate(CertificateBase):
    user_id: int

class Certificate(CertificateBase):
    id: int
    file_path: Optional[str] = None
    user_id: int

    class Config:
        orm_mode = True

