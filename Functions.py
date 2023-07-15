# Miscellaneous information on Python functions

import math

# *args creates a tuple of arguments
def arbitrary(*args):
    for arg in args:
        print(arg, end=' ')

def namedArgs(a, b, c):
    print(a + b + c)

# **kwargs creates a dictionary of arguments
def keywordArgs(**kwargs):
    print('a: ' + kwargs['a'] + ', b: ' + kwargs['b'])

def argTypes(a: int, s: str) -> list:
    return [str(a) + s]

def idFcn():
    # id() returns unique constant for an object
    assert id(None) > 0

    val = id([])
    val2 = id([])
    assert val == val2

def hexFcn():
    # hex() converts integer to hex string
    assert hex(100) == '0x64'
    assert hex(101010101) == '0x6054ab5'

def inputFcn():
    #name = input('Enter your name: ')
    #print('Hello, ' + name)
    pass

def countFcn():
    # count number of values in a container

    # list
    assert [1, 2, 1, 4].count(1) == 2
    assert [1, 2, 1, 4].count(0) == 0

    # tuple
    assert (1, 3).count(3) == 1

def filterFcn():
    # get odd numbers using 'filter'
    result = filter(lambda x : x % 2, [1, 2, 3, 4, 5])
    assert list(result) == [1, 3, 5]

# User vars() to get local variables
def varsFcn():
    a = 1
    b = 2
    v = vars()
    assert list(vars().keys()) == ['a', 'b', 'v']

    # Remove 'a'
    del a
    assert list(vars().keys()) == ['b', 'v']

def dirFcn():
    # dir(obj) gets all attributes and methods for a given object
    listMethods = [x for x in dir([]) if '_' not in x]
    assert 'append' in listMethods
    assert 'clear' in listMethods
    assert 'sort' in listMethods

    mathAttributes = dir(math)
    assert '__name__' in mathAttributes
    assert 'pi' in mathAttributes

def typeFcn():
    t = type(1)   # <class 'int'>
    assert isinstance(1, int)
    t = type('a') # <class 'str'>
    assert isinstance('a', str)
    t = type(1.0) # <class 'float'>
    assert isinstance(1.0, float)

def main():
    arbitrary('a', 'b', 'c')
    namedArgs(a='1', b='2', c='3')
    keywordArgs(a='AA', b='BB')
    out = argTypes(1, 'a')
    assert out == ['1a']
    idFcn()
    hexFcn()
    inputFcn()
    countFcn()
    filterFcn()
    varsFcn()
    dirFcn()
    typeFcn()

if __name__ == '__main__':
    main()
    print('Tests passed!')
