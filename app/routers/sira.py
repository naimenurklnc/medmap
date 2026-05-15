from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.sira import Sira
from datetime import datetime

router = APIRouter(prefix="/sira", tags=["Sıra"])

@router.get("/{poliklinik_id}")
def sira_getir(poliklinik_id: int, db: Session = Depends(get_db)):
    siralar = db.query(Sira).filter(Sira.poliklinik_id == poliklinik_id).all()
    toplam = len(siralar)
    return {
        "poliklinik_id": poliklinik_id,
        "toplam_sira": toplam,
        "tahmini_bekleme": toplam * 4
    }

@router.post("/{poliklinik_id}/sira-al")
def sira_al(poliklinik_id: int, db: Session = Depends(get_db)):
    son_sira = db.query(Sira).filter(
        Sira.poliklinik_id == poliklinik_id
    ).count()
    
    yeni_sira = Sira(
        poliklinik_id=poliklinik_id,
        sira_no=son_sira + 1,
        durum="bekliyor",
        olusturma_zamani=datetime.now()
    )
    
    db.add(yeni_sira)
    db.commit()
    db.refresh(yeni_sira)
    
    return {
        "mesaj": "Sıranız alındı!",
        "sira_no": yeni_sira.sira_no,
        "poliklinik_id": poliklinik_id,
        "tahmini_bekleme": yeni_sira.sira_no * 4,
        "saat": datetime.now().strftime("%H:%M")
    }

@router.get("/{poliklinik_id}/liste")
def sira_listesi(poliklinik_id: int, db: Session = Depends(get_db)):
    siralar = db.query(Sira).filter(Sira.poliklinik_id == poliklinik_id).all()
    return {"siralar": siralar}