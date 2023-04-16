#!/usr/bin/python3
"""
This script will fetch all state obj from the db `hbtn_0e_6_usa` that contain
the letter 'a'
State displayed must be first in states.id
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
    states = session.query(State).filter(State.name.like('%a%'))
    # print results
    for state in states:
        print('{}: {}'.format(state.id, state.name))
