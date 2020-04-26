"""oop.py
"""
class Animal:
    has_blood=True
    can_move=True
    reproduce_sexually=True


class Animal(object):
    # default attributes
    has_blood=True
    can_move=True
    reproduce_sexually=True
    # Initializer / Instance Attributes
    def __init__(self, name):
        self.name = name
