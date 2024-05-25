#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="ali"):
        self._name = None  # Initialize _name attribute
        self.name = name   # Use the setter method for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        elif isinstance(value, str) and len(value) == 0:
            print("Name must be a non-empty string between 1 and 25 characters.")
        else:
            print("Name must be a string between 1 and 25 characters.")

# Test cases
floki = Dog("floki")         # Valid name
empty_name_dog = Dog("")     # Invalid name (empty string)
default_name_dog = Dog()     # Valid default name
short_name_dog = Dog("a")    # Invalid name (too short)
long_name_dog = Dog("a" * 26)  # Invalid name (too long)
