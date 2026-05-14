from fastapi import FastAPI
from app.routers import sira, hastane

app = FastAPI(title="MedMap API", version="1.0.0")

app.include_router(sira.router)
app.include_router(hastane.router)

@app.get("/")
def anasayfa():
    return {"mesaj": "MedMap API çalışıyor!", "versiyon": "1.0.0"}

@app.get("/saglik")
def saglik_kontrolu():
    return {"durum": "aktif"}