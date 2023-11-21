#!/usr/bin/python3
"""Script listing all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

if __name__ == "__main__":
    # first step of connecting to a database
    # Create an engine
    data_source_inf = """mysql+mysqldb://{}:{}@localhost:
                         3306/{}""".format(argv[1], argv[2], argv[3])
    engine = create_engine(data_source_inf)
    # connecting the database
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    states_list = session.query(State).order_by(State.id).all()
    for state in states_list:
        print(str(state.id) + ": " + state.name)
