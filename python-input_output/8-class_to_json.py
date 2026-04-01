#!/usr/bin/python3
"""Module for converting a class instance to a dictionary."""


def class_to_json(obj):
    """Returns the dictionary description of an object for JSON serialization.

    Args:
        obj: The instance of a class.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
