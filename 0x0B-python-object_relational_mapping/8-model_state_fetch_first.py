#!/usr/bin/python3
"""Gets the first state from the table om the hntn_0e_usa
"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker, Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306\
        /{}'.format(sys.argv[1], sys.argv[2],
                    sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()
    if (states):
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
    session.close()
