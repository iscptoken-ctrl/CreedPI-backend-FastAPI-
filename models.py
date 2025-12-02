from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    telegram_id = Column(Integer, unique=True)
    nickname = Column(String)
    wallet = Column(String, default="")
    bcr = Column(Float, default=0)
    cd1 = Column(Float, default=0)
    mvs = Column(Float, default=0)
