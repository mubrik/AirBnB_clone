#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
storage import
"""

from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
