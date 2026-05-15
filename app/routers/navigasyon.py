from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.konum import Oda
import math

router = APIRouter(prefix="/navigasyon", tags=["Navigasyon"])

def mesafe_hesapla(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

@router.post("/oda-ekle")
def oda_ekle(ad: str, kat: int, hastane_id: int, x: float, y: float, tip: str = "muayene", db: Session = Depends(get_db)):
    yeni_oda = Oda(ad=ad, kat=kat, hastane_id=hastane_id, x_koordinat=x, y_koordinat=y, oda_tipi=tip)
    db.add(yeni_oda)
    db.commit()
    db.refresh(yeni_oda)
    return {"mesaj": "Oda eklendi!", "oda": yeni_oda}

@router.get("/odalar/{hastane_id}")
def odalar_listesi(hastane_id: int, db: Session = Depends(get_db)):
    odalar = db.query(Oda).filter(Oda.hastane_id == hastane_id).all()
    return {"odalar": odalar}

@router.get("/yol-tarifi/{hastane_id}")
def yol_tarifi(hastane_id: int, hedef_oda_id: int, mevcut_x: float, mevcut_y: float, db: Session = Depends(get_db)):
    hedef = db.query(Oda).filter(Oda.id == hedef_oda_id, Oda.hastane_id == hastane_id).first()
    if not hedef:
        return {"hata": "Oda bulunamadı"}
    
    mesafe = mesafe_hesapla(mevcut_x, mevcut_y, hedef.x_koordinat, hedef.y_koordinat)
    
    return {
        "hedef_oda": hedef.ad,
        "kat": hedef.kat,
        "mesafe": round(mesafe, 1),
        "yonergeler": [
            f"{hedef.kat}. kata çıkın",
            f"{hedef.ad} odasına gidin",
            f"Tahmini yürüyüş: {round(mesafe * 0.5)} saniye"
        ]
    }