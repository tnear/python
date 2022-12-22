def empty():
    d = {}
    assert isinstance(d, dict)
    assert len(d) == 0

def create():
    d = {1: 2, 'c': 4}
    assert list(d.keys()) == [1, 'c']
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

def keys():
    d = {1: 2, 'c': 4}
    assert list(d.keys()) == [1, 'c']
    assert list(d.values()) == [2, 4]

    # get keys which contain letter 'a'
    m = {'a': 1, 'b': 2, 'ac': 3}
    y = [x for x in list(m.keys()) if 'a' in x]
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
    assert list(d.keys()) == [1, 5]

    # remove last key (5)
    d.popitem()
    assert list(d.keys()) == [1]

def deepCopy():
    d = {1: 2, 'c': 4, 5: 6}
    d2 = d.copy() # deep copy
    d3 = d # reference
    assert d == d2
    assert d is not d2
    assert d is d3

def main():
    empty()
    create()
    find()
    access()
    keys()
    insert()
    comprehension()
    iterate()
    mutate()
    remove()
    deepCopy()

if __name__ == '__main__':
    main()
    print('Tests passed!')
