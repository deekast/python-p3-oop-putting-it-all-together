#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand:str, size:int):
        if type(size) != int:
            print("size must be an integer")
        self.brand = brand
        self.size = size
        self.condition = "New" 

    def cobble(self):
        if self.condition.lower() == "old":
            self.condition = "New"
            print("The shoes have been restored to new condition.")
        else:
            print("Your shoe is as good as new!")

    @property
    def size(self):
        return self._size


    @size.setter
    def size(self, value):
        if type(value) != int:
            print ("size must be an integer")
        self._size = value

