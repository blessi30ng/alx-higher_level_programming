#!/usr/bin/python3
""" Cities in state"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.schema import ForeignKey
from model_state import Base

class City(Base):
    """ Defines ORM class for table with 2 columns"""
    __tablename__ = 'citites'
    id = Column(Integer, autoincrement =True, unique=True,
            nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
