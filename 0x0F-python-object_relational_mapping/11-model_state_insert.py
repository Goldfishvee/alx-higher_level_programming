#!/usr/bin/python3
"""
This script will add the State obj 'Louisiana' to the db `hbtn_0e_6_usa`
The new states.id will be printed after creation
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # create new engine and session
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db_name),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    # create or insert a new State object
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    # print results
    print(new_state.id)
