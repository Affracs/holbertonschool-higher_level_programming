#!/usr/bin/python3
"""
Defines function that checks if object is an instance of or inherits from specified class.
"""
def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of or inherits from a_class, otherwise False.
    """
    return isinstance(obj, a_class)
