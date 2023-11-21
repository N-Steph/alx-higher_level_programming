#!/usr/bin/python3
"""Script that prints the first State object
from the database hbtn_0e_6_usa
"""

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
    result = session.query(State.id, State.name).filter(State.id == 1).first()
    if result is None:
        print("Nothing")
    else:
        print(str(result[0]) + ": " + result[1])
