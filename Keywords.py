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

# Used to make variables accessible in nested functions
def NonLocal():
    x = 10

    def nested():
        nonlocal x  # tells Python to use outer scope's x
        assert x == 10

    nested()

def Raise():
    x = 5
    if x > 5:
        raise Exception('My exception message')

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
    NonLocal()
    Raise()
    Assert()
    With()

if __name__ == '__main__':
    main()
    print('Tests passed!')
