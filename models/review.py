#!/usr/bin/python3
""" Review module for the HBNB project """
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel, Base):
    """ Review classto store review information """
    HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
    __tablename__ = 'reviews'
    if HBNB_TYPE_STORAGE == 'db':
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        text = Column(String(1024), nullable=False)
        store = FileStorage()

        @property
        def reviews(self):
            """Getter attribute for cities class"""
            review_list = []
            for key, value in Review.store.all().items():
                if value['__class__'] == 'City':
                    if value.place_id == self.id:
                        review_list.append(value)
            return review_list

    else:
        place_id = ""
        user_id = ""
        text = ""
