from pydantic import BaseModel
from typing import Optional

class MissionBase(BaseModel):
    name: str
    description: str
    required_certificates: str
    available: bool = True

class MissionCreate(MissionBase):
    pass

class Mission(MissionBase):
    id: int

    class Config:
        orm_mode = True

