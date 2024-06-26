from sqlalchemy import ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State:
    __tablename__ = "states"

    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
