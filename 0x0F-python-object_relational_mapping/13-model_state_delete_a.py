#!/usr/bin/python3

"""deletes state"""

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

    results = session.query(State).filter(State.name.like("%a%")).order_by(State.id)
    for r in results:
        session.delete(r)

    session.commit()
    session.close()
