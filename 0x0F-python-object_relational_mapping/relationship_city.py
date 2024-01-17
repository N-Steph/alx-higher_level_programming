#!/usr/bin/python3

"""
This script contains the model of City table
"""

from sqlalchemy import Column, Integer, String,\
    PrimaryKeyConstraint, UniqueConstraint,\
    ForeignKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """Model of City table
    attribute: id, name, state_id
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id'),
        UniqueConstraint('id'),
        ForeignKeyConstraint(['state_id'], ['states.id'], ondelete='CASCADE')
        )
