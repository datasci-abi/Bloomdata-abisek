'''module docstring'''

import math
import sys


def example1():
    '''function docstring'''
    # THIS IS A LONG COMMENT AND should be
    # wrapped to fit within a 72 character limit
    some_tuple = (1, 2, 3, 'a')
    some_variable = {
        "long": '''LONG CODE LINES should be wrapped within
                   79 characters to prevent page cutoff stuff''',
        "other": [math.pi, 100, 200, 300, 9999292929292,
                  "This IS a long string that looks gross"
                  "and goes beyond what it should"],
        "more": {
            "inner": "THIS whole logical line should be wrapped"
        },
        "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    }

    return (some_tuple, some_variable)


def example_2():
    '''function docstring'''
    return {"is_deprecated": True}


class Example3:
    '''class docstring'''

    def __init__(self, number):
        self.number = number

    def my_method(self):
        '''method docstring'''
        if self.number:
            self.number += 1
            self.number = self.number * self.number
            return self.number
        some_string = """ INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE
        TOUCHED only actual code should be reindented,
        THIS IS MORE CODE
        """
        return (sys.path, some_string)

    def my_method_2(self):
        '''function docstring'''
        return self.number * 10
