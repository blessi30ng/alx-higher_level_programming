#!/usr/bin/python3

"""State object with name passed as an arg"""

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

    results = session.query(State).order_by(state.id)
    for state in results:
        if state.name == argv[4]:
            print("{}".format(state.id))
            found = True
            break
        if found is False:
            print("Not found")
