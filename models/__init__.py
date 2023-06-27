#!/usr/bin/python3
"""
initializes a module by setting its variables and defining its functions
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
