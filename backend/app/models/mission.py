from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from ..database.database import Base

class Mission(Base):
    __tablename__ = "missions"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    required_certificates = Column(String)
    available = Column(Boolean, default=True)

