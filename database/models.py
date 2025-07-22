from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pet(Base):
    __tablename__ = 'pets'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    hunger = Column(Integer)
    energy = Column(Integer)
