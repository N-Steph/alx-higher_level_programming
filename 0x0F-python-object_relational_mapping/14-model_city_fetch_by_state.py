#!/usr/bin/python3

"""
Prints all City objects from the database
hbtn_0e_14_usa
"""

from sqlalchemy import create_engine
from model_city import Base, City
from model_state import Base, State
from sqlalchemy.orm import sessionmaker, Session
import sys

if __name__ == '__main__':
    db_param = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_param.format(sys.argv[1],
                                           sys.argv[2],
                                           sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State, City).\
        filter(City.state_id == State.id).\
        order_by(City.id).all()
    for city in result:
        print('{}: ({}) {}'.format(city[0].name,
                                   city[1].id,
                                   city[1].name))
