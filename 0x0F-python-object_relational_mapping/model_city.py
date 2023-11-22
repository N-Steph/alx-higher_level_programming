#!/usr/bin/python3
"""Definition of City class mapping the city table in hbtn_0e_14_usa
database
"""


from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """model of the city table in hbtn_0e_14_usa database"""
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    states = relationship('State', backref='cities')
