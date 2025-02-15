#!/usr/bin/python3
"""
Module that defines a Student class capable of returning
custom dictionary representations of its instances.
"""


class Student:
    def __init__(self, first_name, last_name, age):

        """
        Initializes the Student instance with the given attributes.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Generates a dictionary representation of the Student instance.
        If a list of attribute names is provided, only those attributes
        are included in the resulting dictionary.

        Args:
            attrs (list, optional): A list of attribute names (strings)
                to include in the dictionary.

        Returns:
            dict: A dictionary containing the specified attributes of
                the Student instance. If no valid attrs list is given,
                all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__
