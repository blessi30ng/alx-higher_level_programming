from sqlalchemy import ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State:
    __tablename__ = "states"
