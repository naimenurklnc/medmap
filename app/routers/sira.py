from fastapi import APIRouter
from datetime import datetime

router = APIRouter(prefix="/sira", tags=["Sıra"])

siralar = {
    1: {"poliklinik": "Dahiliye", "mevcut_sira": 42, "bekleme_dakika": 15},
    2: {"poliklinik": "Kardiyoloji", "mevcut_sira": 18, "bekleme_dakika": 7},
    3: {"poliklinik": "Ortopedi", "mevcut_sira": 63, "bekleme_dakika": 25},
}

@router.get("/")
def tum_siralar():
    return {"siralar": siralar}

@router.get("/{poliklinik_id}")
def sira_getir(poliklinik_id: int):
    if poliklinik_id not in siralar:
        return {"hata": "Poliklinik bulunamadı"}
    return siralar[poliklinik_id]

@router.post("/{poliklinik_id}/sira-al")
def sira_al(poliklinik_id: int):
    if poliklinik_id not in siralar:
        return {"hata": "Poliklinik bulunamadı"}
    
    siralar[poliklinik_id]["mevcut_sira"] += 1
    siralar[poliklinik_id]["bekleme_dakika"] += 4
    
    yeni_sira = siralar[poliklinik_id]["mevcut_sira"]
    
    return {
        "mesaj": "Sıranız alındı!",
        "sira_no": yeni_sira,
        "poliklinik": siralar[poliklinik_id]["poliklinik"],
        "tahmini_bekleme": siralar[poliklinik_id]["bekleme_dakika"],
        "saat": datetime.now().strftime("%H:%M")
    }