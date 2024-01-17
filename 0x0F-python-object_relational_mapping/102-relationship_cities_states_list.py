#!/usr/bin/python3

"""
List all City objects, and corresponding State objects
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':
    db_param = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_param.format(sys.argv[1], sys.argv[2],
                                           sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(City).order_by(City.id).all()
    for city in result:
        print('{}: {} -> {}'.format(city.id, city.name,
                                    city.states.name))
