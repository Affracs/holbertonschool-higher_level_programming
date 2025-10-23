#!/usr/bin/python3
"""
Defines function that checks if object inherits from class but is not an instance of it directly.
"""
def inherits_from(obj, a_class):
    """
    Return True if obj is subclass instance of a_class, else False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
