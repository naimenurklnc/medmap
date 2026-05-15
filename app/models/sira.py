from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Sira(Base):
    __tablename__ = "siralar"

    id = Column(Integer, primary_key=True, index=True)
    poliklinik_id = Column(Integer, nullable=False)
    sira_no = Column(Integer, nullable=False)
    durum = Column(String, default="bekliyor")
    olusturma_zamani = Column(DateTime, default=datetime.now)