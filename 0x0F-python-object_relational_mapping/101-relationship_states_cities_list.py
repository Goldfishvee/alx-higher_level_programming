#!/usr/bin/python3
"""
This script will lidt all State objs and corresponding City objs
from the db `hbtn_0e_101_usa`
Use 'cities' relationship for all 'State' objects
Results must be sorted in ascending order by states.id and cities.id
Results must be displayed as <state id>: <state name>
                             <tabulation><city id>: <city name>
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

    # Execute query
    states = session.query(State).order_by(State.id).all()
    # Print results
    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))

    # clean up
    session.close()
