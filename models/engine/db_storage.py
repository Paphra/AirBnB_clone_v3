#!/usr/bin/python3
"""db_storage module
Contains the DBStorage class
"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
# from models.amenity import Amenity
# from models.review import Review


class DBStorage:
    """DBStorage class
    The Storage for database
    """
    __engine = None
    __session = None

    classes = {
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        # 'Amenity': Amenity,
        # 'Review': Review
    }

    def __init__(self):
        """Initialize everything
        """
        db_user = os.environ.get('HBNB_MYSQL_USER')
        db_pwd = os.environ.get('HBNB_MYSQL_PWD')
        db_host = os.environ.get('HBNB_MYSQL_HOST')
        db_name = os.environ.get('HBNB_MYSQL_DB')
        uri = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            db_user, db_pwd, db_host, db_name
        )
        self.__engine = create_engine(uri, pool_pre_ping=True)
        if os.environ.get('HBNB_ENV') == 'test':
            Base.metadata.reflect(bind=self.__engine)
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """all method
        Returns all the records from the database
        """
        objs = {}
        if cls is None:
            for _cls in DBStorage.classes.values():
                items = self.__session.query(_cls).all()
                for item in items:
                    objs['{}.{}'.format(
                        item.__class__.__name__, item.id)] = item
        else:
            items = self.__session.query(DBStorage.classes[cls]).all()
            for item in items:
                objs['{}.{}'.format(
                    item.__class__.__name__, item.id)] = item
        return objs

    def new(self, obj):
        """new method
        Add the obj to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """save method
        Commit all changes to the db session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete method
        Delete obj from session db if obj is not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload method
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))
