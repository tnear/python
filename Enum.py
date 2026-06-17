# enum — Support for enumerations
# https://docs.python.org/3/library/enum.html

import enum

# create an enumeration
class Color(enum.Enum):
    RED   = 1
    GREEN = 2
    BLUE  = 3

# Python enums must have values. Use auto() to assign
# a unique identifier.
class ColorAutoValues(enum.IntEnum):
    RED = enum.auto()
    GREEN = enum.auto()
    BLUE = enum.auto()

def enum():
    assert isinstance(Color.RED, Color)
    assert Color.RED != Color.GREEN

def value():
    # value property to get numeric value
    assert Color.RED.value == 1

def iterate():
    values = []
    # use 'in' keyword to iterate over all values in enumeration
    for color in Color:
        values.append(color)

    assert values == [Color.RED, Color.GREEN, Color.BLUE]

def auto_values():
    color = ColorAutoValues.RED
    assert color == ColorAutoValues.RED
    assert color != ColorAutoValues.GREEN

def main():
    enum()
    value()
    iterate()
    auto_values()

if __name__ == '__main__':
    main()
    print('Tests passed!')
