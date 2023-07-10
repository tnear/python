import math as m

def As():
    # Creates alias, ex:
    # >>> import math as m
    assert m.pi == 3.141592653589793

def none():
    x = None
    assert x != True
    assert x != False
    assert x is None # preferred over x == None
    assert not x

def Not():
    assert not(1 > 2 and False)
    assert 4 not in (1, 2, 3)

def Is():
    # test if 2 variables refer to same object
    x = [1, 2, 3]
    y = x
    z = [1, 2, 3]

    assert x is y
    assert y is x
    assert x is not z
    assert x == z

def Nonlocal():
    # Used for variables in nested functions
    # ex: https://www.w3schools.com/python/ref_keyword_nonlocal.asp
    pass

def Raise():
    x = 5
    if x > 5:
        raise Exception('My exception')

def simpleGen():
    yield 1
    yield 2
    yield 3

def Yield():
    values = []
    for value in simpleGen():
        values.append(value)

    assert values == [1, 2, 3]

def nextSquare():
    i = 1
    while True:
        yield i * i
        i += 1

def Yield2():
    n = nextSquare()
    assert n.__next__() == 1
    assert n.__next__() == 4
    assert n.__next__() == 9

def Assert():
    # basic assertion
    assert True

    # assertion message, upon failure produces:
    # >  AssertionError: Diagnostic message here
    assert True, 'Diagnostic message here'

def With():
    # see With.py
    pass

def main():
    As()
    none()
    Not()
    Is()
    Nonlocal()
    Raise()
    Yield()
    Yield2()
    Assert()
    With()

if __name__ == '__main__':
    main()
    print('Tests passed!')
