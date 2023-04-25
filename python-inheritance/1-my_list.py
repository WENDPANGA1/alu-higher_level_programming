#!/usr/bin/python3
"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Class MyList inherits list."""

    def print_sorted(self):
        """Prints sorted lists."""
        temp_list = self[:]
        temp_list.sort()
        print("{}".format(temp_list))
