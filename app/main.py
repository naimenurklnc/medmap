from fastapi import FastAPI
from app.database import engine, Base
from app.routers import sira, hastane, navigasyon

Base.metadata.create_all(bind=engine)

app = FastAPI(title="MedMap API", version="1.0.0")

app.include_router(sira.router)
app.include_router(hastane.router)
app.include_router(navigasyon.router)

@app.get("/")
def anasayfa():
    return {"mesaj": "MedMap API çalışıyor!", "versiyon": "1.0.0"}

@app.get("/saglik")
def saglik_kontrolu():
    return {"durum": "aktif"}