#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The User class lives here
"""

from .base_model import BaseModel


class User(BaseModel):
    """Represents a user in the airbnb site
    Attributes:
    - email: email of the user
    - password: Password of the user
    First_name: first name of the user
    -last_name: Last name of the user
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
