#!/usr/bin/python3
"""This module defines a class User"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
    __tablename__ = 'users'
    if HBNB_TYPE_STORAGE == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False, server_default="NULL")
        last_name = Column(String(128), nullable=False, server_default="NULL")
        places = relationship("Place", cascade="delete", backref="user")
        reviews = relationship("Review", cascade="delete", backref="user")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
