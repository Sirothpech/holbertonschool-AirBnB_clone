#!/usr/bin/python3
"""
This module contains the BaseModel class.
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Base class that defines common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        If it's a new instance (not from a dictionary representation),
        adds a call to the new(self) method on storage.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime
                                (value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        Format: "[<class name>] (<self.id>) <self.__dict__>"
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        Calls the save(self) method of storage.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the BaseModel instance to a dictionary representation.
        - Creates a copy of the instance's __dict__.
        - Adds the '__class__' key with the class name of the object.
        - Converts created_at and updated_at to string objects in ISO format.
        Returns:
            A dictionary containing all keys/values of the instance.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data
