#!/usr/bin/python3

""" adds state """

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

    results = session.query(State).order_by(state_id)

    new_state = State(name = 'Louisiana')
    session.add(new_state)
    session.commit()

    result = session.query(State).where(State.name == 'Louisiana')
    for r in results:
        print("{}".format(r.id))
    session.close()
