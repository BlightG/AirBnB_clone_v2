#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBstorage:
    """This class manages the storage of hbnb model in MySql"""
    __engine = None
    __session = None
    HBNB_MYSQL_USER = os.getenv('HBNB_MYSQL_USER')
    HBNB_MYSQL_PWD = os.getenv('HBNB_MYSQL_PWD')
    HBNB_MYSQL_HOST = os.getenv('HBNB_MYSQL_HOST')
    HBNB_MYSQL_DB = os.getenv('HBNB_MYSQL_DB')
    HBNB_ENV = os.getenv('HBNB_ENV')
    classes = [City, State, User]

    def __init__(self):
        """Instanciates a new DBstorage"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(DBstorage.HBNB_MYSQL_USER,
                                                 DBstorage.HBNB_MYSQL_PWD,
                                                 DBstorage.HBNB_MYSQL_HOST,
                                                 DBstorage.HBNB_MYSQL_DB),
            pool_pre_ping=True)
        if DBstorage.HBNB_ENV == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Instance that querys a database session"""

        # searches for all values of an instance of an obj or all objects
        if cls is not None:
            if cls in DBstorage.classes:
                query = self.__session.query(cls).all()
                # print(f'query = {query}')
        else:
            for cls in DBstorage.classes:
                query = self.__session.query(cls).all()
                # print(f'query1 = {query}')

        # appends the query into with key <cls-name>.<object-id>
        cls_dict = {}
        for obj in query:
            cls_dict[f'{obj.__class__.__name__}.{obj.id}'] = obj
        # print(cls_dict)
        return cls_dict

    def new(self, obj):
        """creates a new instance of obj"""
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session if obj is not none"""
        if obj is not None:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """reloads all objs"""
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()
        Base.metadata.create_all(self.__engine)

    def close(self):
        """ call remove() method on the private
            session attribute (self.__session) """
        self.__session.close()
