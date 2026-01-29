#!/usr/bin/python3
"""This module provides a function that adds two integers with strict type validation."""


def add_integer(a, b=98):
    """Adds two integers after casting floats to integers.

    The function verifies that both arguments are integers or floats.
    Floats are cast to integers before the addition.

    Raises:
        TypeError: If a or b is not a valid integer or float.

    Returns:
        The integer sum of a and b.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Reject NaN and Infinity BEFORE casting
    if isinstance(a, float) and (a != a or a in (float('inf'), float('-inf'))):
        raise TypeError("a must be an integer")
    if isinstance(b, float) and (b != b or b in (float('inf'), float('-inf'))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

