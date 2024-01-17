#!/usr/bin/python3

"""
This script defines the State class, which is a model of the state table
in a database
"""

from sqlalchemy import Integer, String,\
    Column, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Model of the state table
       Attributes: id, name
    """

    __tablename__ = 'states'
    id = Column(Integer, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='states', passive_deletes=True)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
        UniqueConstraint('name')
        )
