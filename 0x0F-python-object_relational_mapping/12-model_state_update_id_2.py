#!/usr/bin/python3

""" change name of a state """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).where(State.id == 2)\
            .update({'name': 'New Mexico'}).order_by(State.id)
    session.commit()
    session.close()
