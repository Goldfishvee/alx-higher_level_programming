#!/usr/bin/python3
"""
This script will fetch all state obj from the db `hbtn_0e_6_usa` using
state name input from the command line (must be sql injection free)
Results will display the states.id
If no state has the name searched for, display 'Not found'
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # create new engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    # Execute query
    results = session.query(State).filter_by(name=state_name).first()
    # print results
    if results is not None:
        print(results.id)
    else:
        print('Not found')
