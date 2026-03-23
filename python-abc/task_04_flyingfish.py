#!/usr/bin/env python3
"""Module demonstrating multiple inheritance"""


class Fish:
    """Fish class"""

    def swim(self):
        """Fish swims"""
        print("The fish is swimming")

    def habitat(self):
        """Fish habitat"""
        print("The fish lives in water")


class Bird:
    """Bird class"""

    def fly(self):
        """Bird flies"""
        print("The bird is flying")

    def habitat(self):
        """Bird habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish inherits from Fish and Bird"""

    def swim(self):
        """Override swim"""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat"""
        print("The flying fish lives both in water and the sky!")