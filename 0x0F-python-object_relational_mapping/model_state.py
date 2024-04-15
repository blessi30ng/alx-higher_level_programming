#!/usr/bin/python3
""" 1st state model """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Defines classfor table states, with 2 columns"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True,
            nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
