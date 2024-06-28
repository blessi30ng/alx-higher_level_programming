#!/usr/bin/python3
"""
script that creates the State California with the City San Francisco
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sys import argv

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_s = State(name='California')
    new_c = City(name='San Fransisco')
    new_s.cities.append(new_c)

    session.add(new_s)
    session.add(new_c)
    session.commit()
