#!/usr/bin/python3
"""
This module defines a custom integer class MyInt
that inherits from the built-in int class.
The class overrides the equality comparison methods to
invert their behavior.
"""


class MyInt(int):
    """
    A custom integer class that inherits from int. This class overrides the
    equality (==) and inequality (!=) operators to invert their behavior.
    """

    def __init__(self, value):
        """
        Initializes an instance of MyInt.

        Args:
            value (int): The integer value for the MyInt instance.
        """
        super().__init__()
        self.value = value

    def __eq__(self, other):
        """
        Inverts the behavior of the equality comparison.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: Returns False if the value is equal to the other value.
        """
        return self.value != other

    def __ne__(self, other):
        """
        Inverts the behavior of the inequality comparison.

        Args:
            other (int): The value to compare with.

        Returns:
            bool: Returns True if the value is equal to the other value.
        """
        return self.value == other
