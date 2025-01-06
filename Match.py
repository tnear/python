'''
match statements (Python 3.10) are similar to switch case.
https://docs.python.org/3/tutorial/controlflow.html#tut-match
'''

import dataclasses

def http_code(status):
    out = 'Bad request'
    match status:
        case 400:
            out = 'Bad request'
            # note: there is no fallthrough in match/case.
            # execution leaves after first match
        case 401 | 403:
            # can use '|' to combine multiple values into one line
            out = 'Not allowed'
        case 404:
            out = 'Not found'
        # use '_' wildcard to match all others. Unlike Rust, match
        # statements in Python do not need to be exhaustive.
        case _:
            out = 'Other error'

    return out

def basic():
    print(http_code(400))
    print(http_code(401))
    print(http_code(404))
    print(http_code(499))

# https://www.geeksforgeeks.org/python-match-case-statement/
class Shape:
    pass

@dataclasses.dataclass
class Circle(Shape):
    radius: float

@dataclasses.dataclass
class Rectangle(Shape):
    width: float
    height: float

def check_shape(shape):
    match shape:
        case Circle(radius):
            print(f'Circle radius: {radius}')
        case Rectangle(width, height):
            print(f'Rectangle width: {width}, height: {height}')

def match_class():
    # pattern matching with classes requires either dataclasses (shown)
    # or __match_args__ (not shown).
    circle = Circle(10)
    rectangle = Rectangle(4, 6)
    check_shape(circle)
    check_shape(rectangle)

def main():
    basic()
    match_class()

if __name__ == '__main__':
    main()
    print('Tests passed!')
