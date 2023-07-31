# Tuple: ordered, immutable, allows duplicates
# Can contain different data types

import sys

def empty():
    e = ()
    assert len(e) == 0

    e = tuple() # alt syntax
    assert len(e) == 0

def create():
    t = ('a', 2, 2, '3')
    assert t == ('a', 2, 2, '3')

    oneItem = tuple('a')
    oneItem = ('a',) # one-item needs trailing comma
    assert oneItem == ('a',)

def mutate():
    # tuples are read only, so temp convert to list
    a = (1, 2)
    b = list(a)
    b.append(3)
    a = tuple(b)
    assert a == (1, 2, 3)

def concat():
    a = (1, 2)
    b = ('c', 'd')
    c = a + b
    assert c == (1, 2, 'c', 'd')

def unpack():
    a = (1, 2, 3)
    x, y, z = a
    assert x + y + z == 6

def unpackAll():
    # creates list instead of tuple
    a = (1, 2, 3)
    x, *y = a
    assert x == 1
    assert y == [2, 3]

def comprehension():
    a = tuple(x**2 for x in range(5))
    assert a == (0, 1, 4, 9, 16)

def getsizeof():
    a = [1, 2, 3, 4, 5]
    assert sys.getsizeof(a) == 96

    # tuples are more compact than lists
    b = tuple(a)
    assert sys.getsizeof(b) == 80

def main():
    empty()
    create()
    mutate()
    concat()
    unpack()
    unpackAll()
    comprehension()
    getsizeof()

if __name__ == '__main__':
    main()
    print('Tests passed!')
