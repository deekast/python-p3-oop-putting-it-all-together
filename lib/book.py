#!/usr/bin/env python3
class Book:
    def __init__(self, title:str, page_count:int):
        if type(page_count) != int:
            print ("page_count must be an integer")
        self.title = title
        self._page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if type(value) != int:
            print ("page_count must be an integer")
        self._page_count = value


    def turn_page(self):
        print("Flipping the page...wow, you read fast!")


    
    
        