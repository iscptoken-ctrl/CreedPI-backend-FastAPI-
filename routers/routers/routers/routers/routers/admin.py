from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

router = APIRouter(prefix="/admin", tags=["Admin"])

def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all-users")
def get_all_users(db: Session = Depends(db)):
    return db.query(User).all()
