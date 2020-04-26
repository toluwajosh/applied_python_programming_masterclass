"""oop.py
"""


class Animal(object):
    # default attributes
    has_blood = True
    can_move = True
    reproduce_sexually = True
    # Initializer / Instance Attributes
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, age, color):
        self.name = name
        self.color = color

    # a function to introduce the class instance
    def introduce(self):  # may or may not take an argument
        print("I am ", self.name, ".Nice to meet you.")
