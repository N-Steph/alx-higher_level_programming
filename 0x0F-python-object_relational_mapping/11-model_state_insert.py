#!/usr/bin/python3
"""Adding State object "Louisiana" to the database hbtn_0e_6_usa"""

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
    state_obj = State(name='Louisiana')
    session.add(state_obj)
    session.commit()
    print(state_obj.id)
