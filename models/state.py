#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

    # if storage is a database or filestorage
    if HBNB_TYPE_STORAGE == 'db':
        from sqlalchemy import Column, String
        from sqlalchemy.orm import relationship
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="delete", backref="state")
    else:
        name = ""
        store = FileStorage()

        @property
        def cities(self):
            """Getter attribute for cities class"""
            city_list = []
            for key, value in State.store.all().items():
                if value['__class__'] == 'City':
                    if value.state_id == self.id:
                        city_list.append(value)
            return city_list
