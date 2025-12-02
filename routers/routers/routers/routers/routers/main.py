from fastapi import FastAPI
from database import Base, engine
from routers import users, wallet, admin

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(wallet.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"msg": "BNB Heroes Backend Active!"}
