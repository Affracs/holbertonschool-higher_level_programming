#!/usr/bin/env python3
"""Module demonstrating mixins"""


class SwimMixin:
    """Mixin for swimming ability"""

    def swim(self):
        """Swim method"""
        print("The creature swims!")


class FlyMixin:
    """Mixin for flying ability"""

    def fly(self):
        """Fly method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class combining multiple abilities"""

    def roar(self):
        """Dragon roar"""
        print("The dragon roars!")