#!/usr/bin/python3
""" definition of a city """
from relationship_state import Base
from sqlalchemy import Integer, Column, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

class City(Base):
    """ defines each city """
    __tablename__ == 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id =  Column(Integer, ForeignKey("states.id"), nullable=False)
