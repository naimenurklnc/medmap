from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Oda(Base):
    __tablename__ = "odalar"

    id = Column(Integer, primary_key=True, index=True)
    ad = Column(String, nullable=False)
    kat = Column(Integer, nullable=False)
    hastane_id = Column(Integer, nullable=False)
    x_koordinat = Column(Float, nullable=False)
    y_koordinat = Column(Float, nullable=False)
    oda_tipi = Column(String, default="muayene")