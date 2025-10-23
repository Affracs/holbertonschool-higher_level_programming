#!/usr/bin/python3
"""
Defines MyList class that inherits from list and adds method to print list sorted.
"""
class MyList(list):
    """
    Custom list class that can print itself sorted.
    """
    def print_sorted(self):
        """
        Print the list elements in ascending sorted order without modifying the list.
        """
        print(sorted(self))
