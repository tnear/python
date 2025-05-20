# Python's primary associative array
# https://docs.python.org/3/tutorial/datastructures.html

def empty():
    d = {}
    assert isinstance(d, dict)
    assert len(d) == 0

def create():
    d = {1: 2, 'c': 4}
    # note: dict.keys() is rarely needed:
    assert list(d) == [1, 'c'] # list(d) is same as list(d.keys())
    assert list(d.values()) == [2, 4]

def find():
    d = {1: 2, 'c': 4}
    assert 1 in d
    assert 'c' in d
    assert 2 not in d

def access():
    d = {1: 2, 'c': 4}
    assert d[1] == 2
    assert d['c'] == 4

def keysMethod():
    d = {1: 2, 'c': 4}
    assert list(d) == [1, 'c']
    assert list(d.values()) == [2, 4]

    # get keys which contain letter 'a'
    m = {'a': 1, 'b': 2, 'ac': 3}
    y = [x for x in list(m) if 'a' in x]
    assert y == ['a', 'ac']

def insert():
    d = {1: 2, 'c': 4}
    d['new_key'] = 11
    assert d['new_key'] == 11

def comprehension():
    x = {num : num**2 for num in range(1, 6)}
    assert x == {1: 1, 2:4, 3:9, 4:16, 5:25}

def iterate():
    keys = []
    values = []
    d = {1: 2, 'c': 4}
    for key, val in d.items():
        keys.append(key)
        values.append(val)

    assert keys == [1, 'c']
    assert values == [2, 4]

def mutate():
    d = {1: 2}
    d[1] = 3
    assert d[1] == 3

def remove():
    d = {1: 2, 'c': 4, 5: 6}

    # remove key 'c'
    d.pop('c')
    assert list(d) == [1, 5]

    # remove last key (5)
    d.popitem()
    assert list(d) == [1]

def deepCopy():
    d = {1: 2, 'c': 4, 5: 6}
    d2 = d.copy() # deep copy
    d3 = d # reference
    assert d == d2
    assert d is not d2
    assert d is d3

# Return length/size of dictionary
def size():
    d = {1: 2, 'c': 4, 5: 6}
    assert len(d) == 3

# Python 3.9
def merge():
    # use the update() method to merge two dictionaries
    a = {'a': 1, 'b': 2}
    b = {'hello': 'world'}
    a.update(b)
    assert a == {'a': 1, 'b': 2, 'hello': 'world'}

    # union operator (|)
    a = {'y': 25, 'z': 26}
    c = a | b
    assert c == {'y': 25, 'z': 26, 'hello': 'world'}
    # in-place union (|=)
    a |= b
    assert a == {'y': 25, 'z': 26, 'hello': 'world'}

def get():
    d = {'a': 10, 'b': 20}
    assert d.get('a') == 10

    # when get() cannot find the key, it returns None
    result = d.get('fake')
    assert result is None

    # the 2nd argument (optional) specified a default value if value does not exist
    defaultValue = 101
    assert d.get('fake', defaultValue) == defaultValue

def hashListUsingTuple():
    # lists cannot be hashed because they are mutable
    # however, you can instead convert the list to a tuple
    d = {}
    a = [0, 2, 3]
    # d[a] = True # <-- errors because list is unhashable

    d[tuple(a)] = True # works because tuple is immutable

    assert d[tuple(a)] == True

def sort():
    d = {'apple': 5, 'orange': 3, 'banana': 2, 'grape': 4}

    # sort a dictionary by values in descending order
    sortedDict = sorted(d.items(), key=lambda item: item[1], reverse=True)
    assert sortedDict[0] == ('apple', 5)
    assert sortedDict[1] == ('grape', 4)
    assert sortedDict[2] == ('orange', 3)
    assert sortedDict[3] == ('banana', 2)

    # sort a dictionary keys
    # note: do not call sorted(d.keys()) because dictionaries iterate over keys by default, ex:
    # for key in d:
    #     ...
    sortedDict = sorted(d)
    assert sortedDict == ["apple", "banana", "grape", "orange"]

def flatten_to_list():
    # use list(dict.items()) to flatten a dictionary into a list
    # of name/value pairs
    d = {'a': 1, 'b': 2, 'c': 'three'}
    flattened = list(d.items())

    exp = [('a', 1), ('b', 2), ('c', 'three')]
    assert flattened == exp

def main():
    empty()
    create()
    find()
    access()
    keysMethod()
    insert()
    comprehension()
    iterate()
    mutate()
    remove()
    deepCopy()
    size()
    merge()
    get()
    hashListUsingTuple()
    sort()
    flatten_to_list()

if __name__ == '__main__':
    main()
    print('Tests passed!')
