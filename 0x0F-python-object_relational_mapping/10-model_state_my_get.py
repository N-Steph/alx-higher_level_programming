#!/usr/bin/python3
"""Script that prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    data_source_inf = """mysql+mysqldb://{}:{}@localhost:
                         3306/{}""".format(argv[1], argv[2], argv[3])
    # Creating Engine object
    engine = create_engine(data_source_inf)
    engine.connect()
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter(State.name == argv[4]).first()
    if result is None:
        print("Not found")
    else:
        print(result.id)
