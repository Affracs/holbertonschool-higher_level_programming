#!/usr/bin/python3
"""This module provides a function that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers after casting floats to integers.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        The integer sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

