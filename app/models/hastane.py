from sqlalchemy import Column, Integer, String
from app.database import Base

class Hastane(Base):
    __tablename__ = "hastaneler"

    id = Column(Integer, primary_key=True, index=True)
    ad = Column(String, nullable=False)
    adres = Column(String)
    telefon = Column(String)

class Poliklinik(Base):
    __tablename__ = "poliklinikler"

    id = Column(Integer, primary_key=True, index=True)
    ad = Column(String, nullable=False)
    kat = Column(Integer)
    hastane_id = Column(Integer, nullable=False)