#!/usr/bin/python3
"""Module for the State class"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """The State class"""
    __tablename__ = 'states'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True, unique=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String(128), nullable=False)
    cities = sqlalchemy.orm.relationship("City", back_populates="state")
