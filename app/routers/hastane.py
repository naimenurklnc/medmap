from fastapi import APIRouter

router = APIRouter(prefix="/hastane", tags=["Hastane"])

hastaneler = {
    1: {
        "ad": "Antalya Eğitim ve Araştırma Hastanesi",
        "adres": "Varlık Mah. Kazım Karabekir Cad.",
        "telefon": "0242 249 44 00",
        "poliklinikler": [
            {"id": 1, "ad": "Dahiliye", "kat": 2},
            {"id": 2, "ad": "Kardiyoloji", "kat": 3},
            {"id": 3, "ad": "Ortopedi", "kat": 4},
            {"id": 4, "ad": "Nöroloji", "kat": 2},
        ]
    }
}

@router.get("/")
def tum_hastaneler():
    return {"hastaneler": list(hastaneler.values())}

@router.get("/{hastane_id}")
def hastane_getir(hastane_id: int):
    if hastane_id not in hastaneler:
        return {"hata": "Hastane bulunamadı"}
    return hastaneler[hastane_id]

@router.get("/{hastane_id}/poliklinikler")
def poliklinikler_getir(hastane_id: int):
    if hastane_id not in hastaneler:
        return {"hata": "Hastane bulunamadı"}
    return {"poliklinikler": hastaneler[hastane_id]["poliklinikler"]}