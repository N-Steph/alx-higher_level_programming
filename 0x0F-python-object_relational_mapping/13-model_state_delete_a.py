#!/usr/bin/python3
"""Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_connect_inf = """mysql+mysqldb://{}:{}@localhost:
                        3306/{}""".format(argv[1], argv[2], argv[3])
    engine = create_engine(db_connect_inf)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    state_obj = session.query(State).filter(State.name.like("%a%"))
    for obj in state_obj:
        session.delete(obj)
    session.commit()
