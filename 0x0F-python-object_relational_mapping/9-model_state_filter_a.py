#!/usr/bin/python3

"""
List all State object tht contain the letter 'a'
from  the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
import sys

if __name__ == '__main__':
    db_param = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(db_param.format(sys.argv[1],
                                           sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name.like('%a%')).all()
    for state in result:
        print('{}: {}'.format(state.id, state.name))
