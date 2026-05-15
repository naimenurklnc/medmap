from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.hastane import Hastane, Poliklinik

router = APIRouter(prefix="/hastane", tags=["Hastane"])

@router.get("/")
def tum_hastaneler(db: Session = Depends(get_db)):
    hastaneler = db.query(Hastane).all()
    return {"hastaneler": hastaneler}

@router.get("/{hastane_id}")
def hastane_getir(hastane_id: int, db: Session = Depends(get_db)):
    hastane = db.query(Hastane).filter(Hastane.id == hastane_id).first()
    if not hastane:
        return {"hata": "Hastane bulunamadı"}
    return hastane

@router.get("/{hastane_id}/poliklinikler")
def poliklinikler_getir(hastane_id: int, db: Session = Depends(get_db)):
    poliklinikler = db.query(Poliklinik).filter(
        Poliklinik.hastane_id == hastane_id
    ).all()
    return {"poliklinikler": poliklinikler}

@router.post("/ekle")
def hastane_ekle(ad: str, adres: str, telefon: str, db: Session = Depends(get_db)):
    yeni_hastane = Hastane(ad=ad, adres=adres, telefon=telefon)
    db.add(yeni_hastane)
    db.commit()
    db.refresh(yeni_hastane)
    return {"mesaj": "Hastane eklendi!", "hastane": yeni_hastane}

@router.post("/{hastane_id}/poliklinik-ekle")
def poliklinik_ekle(hastane_id: int, ad: str, kat: int, db: Session = Depends(get_db)):
    yeni_poliklinik = Poliklinik(ad=ad, kat=kat, hastane_id=hastane_id)
    db.add(yeni_poliklinik)
    db.commit()
    db.refresh(yeni_poliklinik)
    return {"mesaj": "Poliklinik eklendi!", "poliklinik": yeni_poliklinik}
