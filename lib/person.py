#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=""):
        self._name = None  # Initialize _name attribute
        self.name = name   # Use the setter method for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case and save
        elif isinstance(value, str) and len(value) == 0:
            print("Name must be a non-empty string between 1 and 25 characters.")
        else:
            print("Name must be a string between 1 and 25 characters.")

# Test cases
person1 = Person("john doe")         # Valid name, converted to title case
empty_name_person = Person("")       # Invalid name (empty string)
default_name_person = Person()       # Valid default name (empty string)
short_name_person = Person("a")      # Invalid name (too short)
long_name_person = Person("a" * 26)  # Invalid name (too long)

