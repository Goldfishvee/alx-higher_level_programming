#!/usr/bin/python3
"""
This script will list all City objs from the db `hbtn_0e_101_usa`
Use 'state' relationship to access 'State' obj linked to the 'City'
Results must be sorted in ascending order by cities.id
Results must be displayed as <city id>: <city name> -> <state name>
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
    cities = session.query(City).join(State).order_by(City.id).all()
    # Print results
    for city in cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.states.name))

    # clean up
    session.close()
