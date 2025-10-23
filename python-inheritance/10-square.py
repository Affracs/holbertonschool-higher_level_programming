#!/usr/bin/python3
"""
Defines Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Class representing square using Rectangle inheritance.
    """
    def __init__(self, size):
        """
        Initialize square with validated size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Return area of square.
        """
        return self.__size ** 2
