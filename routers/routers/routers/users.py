from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import User

router = APIRouter(prefix="/users", tags=["Users"])

def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register_user(telegram_id: int, nickname: str, db: Session = Depends(db)):
    user = db.query(User).filter(User.telegram_id == telegram_id).first()
    if not user:
        user = User(telegram_id=telegram_id, nickname=nickname)
        db.add(user)
        db.commit()
    return {"status": "ok"}
