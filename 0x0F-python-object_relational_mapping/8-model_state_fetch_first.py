#!/usr/bin/python3
"""
This script will fetch the first state obj from the db `hbtn_0e_6_usa`
State displayed must be first in states.id
No fetching all states from db before result display
If table `states` is empty, print `Nothing`
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
    states = session.query(State).order_by(State.id).first()
    # print results
    if states is None:
        print('Nothing')
    else:
        print('{}: {}'.format(states.id, states.name))
