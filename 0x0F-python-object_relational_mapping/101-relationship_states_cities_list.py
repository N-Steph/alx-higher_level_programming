#!/usr/bin/python3

"""
List all State objects, and corresponding City objects
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
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).\
        filter(City.state_id == State.id).\
        order_by(State.id, City.state_id).all()
    for record in result:
        print('{}: {}'.format(record[0].id, record[0].name))
        for city in record[0].cities:
            print('    {}: {}'.format(city.id, city.name))
