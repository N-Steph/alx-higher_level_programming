#!/usr/bin/python3

"""
Creates the State "California" with the City
"San Francisco" from the database hbnt_0e_100_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':
    db_param = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_param.format(sys.argv[1],
                                           sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_cities = City(name='San Francisco')
    new_state = State(name='California', cities=[new_cities])
    session.add(new_state)
    session.commit()
