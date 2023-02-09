#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
the State class lives here
"""

from .base_model import BaseModel


class State(BaseModel):
    """Represents a state in the airbnb site
    Attributes:
    - name: name of state
    """
    name = ''
