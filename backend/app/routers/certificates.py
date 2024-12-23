from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from ..schemas import certificate as certificate_schema
from ..crud import certificate as certificate_crud
from ..dependencies.auth import get_current_user, get_db
import os
from ..config.settings import settings
from ..tasks.background_tasks import process_certificate

router = APIRouter(
    prefix="/certificates",
    tags=["certificates"],
    dependencies=[Depends(get_current_user)],
)

@router.post("/", response_model=certificate_schema.Certificate)
def create_certificate(certificate: certificate_schema.CertificateCreate, file: UploadFile = File(None), db: Session = Depends(get_db)):
    file_path = None
    if file:
        file_location = os.path.join("app", "static", "uploads", file.filename)
        with open(file_location, "wb") as f:
            f.write(file.file.read())
        file_path = file_location
    created_certificate = certificate_crud.create_certificate(db=db, certificate=certificate, file_path=file_path)
    process_certificate.delay(created_certificate.id)
    return created_certificate

@router.get("/user/{user_id}", response_model=List[certificate_schema.Certificate])
def read_certificates(user_id: int, db: Session = Depends(get_db)):
    return certificate_crud.get_certificates_by_user(db=db, user_id=user_id)

@router.get("/{certificate_id}", response_model=certificate_schema.Certificate)
def read_certificate(certificate_id: int, db: Session = Depends(get_db)):
    db_certificate = certificate_crud.get_certificate(db=db, certificate_id=certificate_id)
    if db_certificate is None:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return db_certificate

