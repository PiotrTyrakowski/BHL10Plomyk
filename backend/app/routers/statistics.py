from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud import user as user_crud, mission as mission_crud
from ..dependencies.auth import get_current_active_admin, get_db
from typing import Dict

router = APIRouter(
    prefix="/statistics",
    tags=["statistics"],
    dependencies=[Depends(get_current_active_admin)],
)

@router.get("/missions_per_user")
def missions_per_user(db: Session = Depends(get_db)):
    users = user_crud.get_users(db)
    data = {user.username: len(user.certificates) for user in users}
    return data

@router.get("/mission_availability")
def mission_availability(db: Session = Depends(get_db)):
    missions = mission_crud.get_missions(db)
    available = sum(m.available for m in missions)
    total = len(missions)
    return {"available": available, "total": total}

