#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Includes the class Review Model
"""
from .base_model import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""
    user_id = ""
    text = ""
