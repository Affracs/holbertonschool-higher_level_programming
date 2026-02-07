#!/usr/bin/python3
"""Function that returns true if object is instance of class that inherited from specified class, else false"""


def inherits_from(obj, a_class):
    """Return true if obj = instance of subclass of a_class"""
    return isinstance(obj,a_class) and type(obj) is not a_class
