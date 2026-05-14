# MedMap 🏥

Hastane içi navigasyon ve sıra takip uygulaması.

## Özellikler
- Gerçek zamanlı sıra takibi
- Hastane içi yön bulma
- Poliklinik bilgilendirme
- Anlık bildirimler

## Teknolojiler
- **Backend:** Python, FastAPI
- **Mobil:** Flutter
- **Veritabanı:** PostgreSQL
- **Konum:** BLE Beacon / RTLS

## Kurulum
```bash
pip install fastapi uvicorn
uvicorn app.main:app --reload
```

## API Endpoints
| Method | URL | Açıklama |
|--------|-----|----------|
| GET | /sira/{id} | Sıra bilgisi |
| POST | /sira/{id}/sira-al | Sıra al |
| GET | /hastane/{id} | Hastane bilgisi |
| GET | /hastane/{id}/poliklinikler | Poliklinik listesi |
