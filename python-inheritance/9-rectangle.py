#!/usr/bin/python3
"""
Defines Rectangle class with area and string representation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle that extends BaseGeometry with area and print features.
    """
    def __init__(self, width, height):
        """
        Initialize Rectangle with validated width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Return area of rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return formatted string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
