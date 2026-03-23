#!/usr/bin/env python3
"""Module defines Shape abstract class and implementations"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate area"""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter"""
        pass


class Circle(Shape):
    """Circle class"""

    def __init__(self, radius):
        """Initialize circle with radius"""
        self.radius = radius

    def area(self):
        """Return area of circle"""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Return perimeter (circumference)"""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, width, height):
        """Initialize rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape (duck typing)"""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())