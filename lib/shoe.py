#!/usr/bin/env python3


class Shoe:
    def __init__(self, brand=None, size=None):
        self._brand = brand
        self._size = size
        self._condition = "Used"

    def get_brand(self):
        return self._brand

    def get_size(self):
        return self._size

    def set_size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    def get_condition(self):
        return self._condition

    def cobble(self):
        print("Your shoe is as good as new!")
        self._condition = "New"

    brand = property(get_brand)
    size = property(get_size, set_size)
    condition = property(get_condition)
