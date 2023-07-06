#!/usr/bin/python3
"""
This module contains the City class inherit from the BaseModel class.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class"""
    state_id = ""
    name = ""
