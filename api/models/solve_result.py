from sqlalchemy import Column, Integer, Float, String, DateTime

from api.db import Base

class SolveResult(Base):
    __tablename__ = "solves"
    
    id = Column(Integer, primary_key=True)
    time = Column(Float)
    scramble = Column(String(1024))
    comment = Column(String(1024))
    date = Column(DateTime)
