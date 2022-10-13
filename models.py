from sqlalchemy import Column, Integer, String
from database import Base 

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    # uuid creates a unique id for each item
    task = Column(String(256))