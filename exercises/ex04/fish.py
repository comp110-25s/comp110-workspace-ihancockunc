"""File to define Fish class."""

__author__: str = "730608493"


class Fish:
    age: int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self):
        self.age += 1
        return None
