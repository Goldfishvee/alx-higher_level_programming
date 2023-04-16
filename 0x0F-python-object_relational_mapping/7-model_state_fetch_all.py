#!/usr/bin/python3
"""
This script will fetch all state data from the db `hbtn_0e_6_usa`
Results will be sorted in ascending order by states.id
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    # create new engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    # Execute query
    states = session.query(State).order_by(State.id).all()
    # print results
    for state in states:
        print('{}: {}'.format(state.id, state.name))
