# List: ordered, mutable, allows duplicates
# Can contain different data types

import sys
from copy import deepcopy
import itertools

def empty():
    e = []
    assert len(e) == 0
    e = list() # alt syntax
    assert len(e) == 0

def creation():
    a = ['a', 2, 'c', 'c']
    assert a[0] == 'a'

def preallocate():
    a = [False] * 5
    assert a == [False, False, False, False, False]

def mutate():
    # single element
    a = [1, 2, 3, 4]
    a[1] = 2.2
    assert a[1] == 2.2

    # multiple elements
    a[1:2] = ['one', 'two']
    assert a[1] == 'one'
    assert a[2] == 'two'

    # truncate to [1, 0]
    a[1:] = [0]
    assert len(a) == 2

def find():
    a = [1, 2, 3, 4, 5]
    assert 1 in a
    assert 0 not in a

def append():
    # +=
    a = [1, 2]
    a += [3]
    assert a == [1, 2, 3]

    # append method
    a.append(4)
    assert a == [1, 2, 3, 4]

def insert():
    a = ['a', 'b', 'd']
    a.insert(2, 'c')
    assert a == ['a', 'b', 'c', 'd']

def concatenate():
    a = [1, 2]
    b = [3]
    c = a + b
    assert c == [1, 2, 3]

    a.extend(b)
    assert a == [1, 2, 3]

def unpack():
    a = [1, 2, 3]
    x, y, z = a
    assert x == 1
    assert y == 2
    assert z == 3

def unpackRemainder():
    a = [1, 2, 3]
    x, *y = a
    assert x == 1
    assert y == [2, 3]

def funcArg(a, b, c):
    assert a == 1
    assert b == 2
    assert c == 3

def unpackFuncArg():
    a = [1, 2, 3]
    funcArg(*a)

def remove():
    a = ['a', 'b', 'c']
    a.remove('b')
    assert a == ['a', 'c']

def pop():
    # remove index
    a = [1, 2, 3, 4]
    a.pop(2)
    assert a == [1, 2, 4]

    # remove end
    a.pop()
    assert a == [1, 2]

def clear():
    a = [1, 2]
    a.clear()
    assert len(a) == 0

def comprehension():
    # list = [expr for item in <iter> if [condition]]

    # square numbers in range
    y = [x ** 2 for x in range(9)]
    assert y == [0, 1, 4, 9, 16, 25, 36, 49, 64]

    # get all strings containing 'a':
    strs = ['ab', 'cd', 'ea', 'zz']
    y = [x for x in strs if 'a' in x]
    assert y == ['ab', 'ea']

    # get odd numbers
    n = list(range(11))
    y = [x for x in n if x % 2]
    assert y == [1, 3, 5, 7, 9]

    # convert strings to uppercase
    s = ['ab', 'cD', 'EF']
    u = [x.upper() for x in s]
    assert u == ['AB', 'CD', 'EF']

    # get public methods for list
    result = [x for x in dir([]) if '_' not in x]
    assert len(result) > 0

    # (alt) get public methods for list
    result = [x for x in dir([]) if not x.startswith('_')]
    assert len(result) > 0

def shallowCopy():
    a = [1, 2, 3]
    b = a.copy()
    c = a[:]
    assert a is not b
    assert a is not c

    # note: list1 = list2 creates a reference
    d = a
    assert a is d

def deepCopy():
    a = [1, 2, 3]
    b = deepcopy(a)
    assert a == b

def replicate():
    a = [1, 'b']
    a *= 3
    assert a == [1, 'b', 1, 'b', 1, 'b']

def bytes():
    a = [1, 2, 3, 4, 5]
    bytes = sys.getsizeof(a)
    assert bytes == 104 # was 96 earlier

def index():
    # Find first element and return its index
    a = [4, 3, 2, 3]
    idx = a.index(3)
    assert idx == 1

    # Throws ValueError if item is not in container
    # a.index('fake_index')

def sort():
    a = [4, 2, 1, 3]
    a.sort()
    assert a == [1, 2, 3, 4]

    # key allows custom sort order
    a = ['aa', 'b', 'ccc']
    # sort by string length (ascending)
    a.sort(key = lambda item: len(item))
    assert a == ['b', 'aa', 'ccc']

def unique():
    # get unique elements in a list using set() constructor
    a = [2, 1, 2, 4, 4]
    unique = list(set(a))
    assert unique == [1, 2, 4]

def flatten():
    # flatten 2D list (matrix) using chain()
    matrix = [ [2, 3], [4, 5], [1, 2] ]

    result = list(itertools.chain(*matrix))
    assert result == [2, 3, 4, 5, 1, 2]

def count():
    a = [3, 1, 2, 1, 1]
    assert a.count(1) == 3
    assert a.count(3) == 1
    assert a.count(9) == 0

def findDuplicates():
    # note: removing duplicates is easier, just copy list -> set -> list
    # the example shows how to find which elements are in the list multiple times

    # create a list with duplicate elements
    items = [3, 1, 2, 4, 2, 1, 0]

    # keep track of which elements have been seen
    seen = set()
    duplicates = set()
    for item in items:
        if item in seen:
            duplicates.add(item) # seen before, add to duplicate list
        seen.add(item)

    duplicateList = list(duplicates)
    assert duplicateList == [1, 2]

def main():
    empty()
    creation()
    preallocate()
    mutate()
    find()
    append()
    insert()
    concatenate()
    unpack()
    unpackRemainder()
    unpackFuncArg()
    remove()
    pop()
    clear()
    comprehension()
    shallowCopy()
    deepCopy()
    replicate()
    bytes()
    index()
    sort()
    unique()
    flatten()
    count()
    findDuplicates()

if __name__ == '__main__':
    main()
    print('Tests passed!')
