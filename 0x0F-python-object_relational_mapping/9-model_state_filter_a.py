#!/usr/bin/python3
"""Script that lists all State object containing the letter a"""

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
    result = session.query(State.id, State.name).filter(State.name.like("%a%"))
    for obj in result:
        print(str(obj.id) + ": " + obj.name)
