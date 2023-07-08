# enum — Support for enumerations
# https://docs.python.org/3/library/enum.html

import enum

# create an enumerationn
class Color(enum.Enum):
    RED   = 1
    GREEN = 2
    BLUE  = 3

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

def main():
    enum()
    value()
    iterate()

if __name__ == '__main__':
    main()
    print('Tests passed!')
