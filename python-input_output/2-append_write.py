#!/usr/bin/python3
"""Module to append a string at the end of a text"""



def append_write(filename="", text=""):
    """Appends a string at the end of a UTF-8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
