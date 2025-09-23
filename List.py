# List: ordered, mutable, allows duplicates
# Can contain different data types

from collections import Counter
from copy import deepcopy
import itertools
import sys

def empty():
    e = []
    assert len(e) == 0
    # e = list() # alt syntax (not recommended)

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
    # '+=' operator
    a = [1, 2]
    a += [3]
    assert a == [1, 2, 3]

    # alt syntax: append method
    a.append(4)
    assert a == [1, 2, 3, 4]

# insert() has to shift all elements after, O(n) worst-case
def insert():
    a = ['a', 'b', 'd']
    # insert 'c' at index 2
    a.insert(2, 'c')
    assert a == ['a', 'b', 'c', 'd']

    # insert at beginning of list using insert()
    a.insert(0, '0')
    assert a == ['0', 'a', 'b', 'c', 'd']

    # insert at beginning using list concatenation (creates new list, also O(n))
    a = [2, 3, 4]
    a = [1] + a
    assert a == [1, 2, 3, 4]

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
    # pass (1, 2, 3) as comma separated list using '*' operator
    funcArg(*a)

def remove():
    # remove() removes the first element with that value (not all)
    a = ['a', 'b', 'c', 'b']
    a.remove('b')
    assert a == ['a', 'c', 'b']

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

    # because 'a' is distinct from 'b', changing it does not impact 'b'
    a[0] = 0
    assert a != b

def replicate():
    a = [1, 'b']
    a *= 3
    assert a == [1, 'b', 1, 'b', 1, 'b']

def bytes_example():
    a = [1, 2, 3, 4, 5]
    b = sys.getsizeof(a)
    assert b == 104 # was 96 earlier

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
    a.sort(key=len)
    assert a == ['b', 'aa', 'ccc']

def unique():
    # get unique elements in a list using set() constructor
    a = [2, 1, 2, 4, 4]
    unique_values = list(set(a))
    assert unique_values == [1, 2, 4]

def flatten():
    # flatten 2D list (matrix) using chain()
    matrix = [ [2, 3], [4, 5], [1, 2] ]

    result = list(itertools.chain(*matrix))
    assert result == [2, 3, 4, 5, 1, 2]

def count():
    # count() is a linear operation. Use collections.Counter for efficiency.
    a = [3, 1, 2, 1, 1]
    assert a.count(1) == 3
    assert a.count(3) == 1
    assert a.count(9) == 0

def findDuplicates():
    # note: removing duplicates is easier, just copy list -> set -> list
    # the example shows how to find which elements are in the list multiple times

    # create a list with duplicate elements
    items = [3, 1, 2, 4, 2, 1, 0]

    # use Counter to track each element's count.
    # (note: do not use list.count because it is a linear scan)
    duplicates = [item for item, count in Counter(items).items() if count > 1]
    assert duplicates == [1, 2]

def next_example():
    nums = [1, 2, 3, 4, 5]
    # get first even number using next()
    first_even = next(x for x in nums if x % 2 == 0)
    assert first_even == 2

    # alt syntax (not recommended b/c it creates and throws away a temp list)
    #first_even = [x for x in nums if x % 2 == 0][0]
    #assert first_even == 2

    # the optional second argument to next() provides a default value
    no_data = next((x for x in nums if x > 100), None)
    assert no_data is None

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
    bytes_example()
    index()
    sort()
    unique()
    flatten()
    count()
    findDuplicates()
    next_example()

if __name__ == '__main__':
    main()
    print('Tests passed!')
