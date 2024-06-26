#!/usr/bin/python3

""" City """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City.id, City).filter(
        City.state_id == State.id).order_by(City.id).all()

    for r in results:
        print("{}: {} {}".format(r.State.name, r.id, r.City.name))
    session.close()
