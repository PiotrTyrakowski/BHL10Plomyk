from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas import mission as mission_schema
from ..crud import mission as mission_crud, user as user_crud
from ..dependencies.auth import get_current_user, get_db

router = APIRouter(
    prefix="/recommendations",
    tags=["recommendations"],
    dependencies=[Depends(get_current_user)],
)

@router.get("/user/{user_id}", response_model=List[mission_schema.Mission])
def get_recommendations(user_id: int, db: Session = Depends(get_db)):
    user = user_crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user_certs = set(cert.name for cert in user.certificates)
    missions = mission_crud.get_missions(db)
    recommended = []
    for mission in missions:
        required = set(mission.required_certificates.split(","))
        if required.issubset(user_certs) and mission.available:
            recommended.append(mission)
    return recommended

