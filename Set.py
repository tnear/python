# Set
# Unordered, immutable, unindexed
# No duplicates

def empty():
    e = set() # no alt syntax
    assert len(e) == 0

def create():
    s = {1, 'b'}
    assert s == {1, 'b'}

    # duplicates are automatically removed
    s = {1, 'b', 'b', 1}
    assert s == {1, 'b'}

def find():
    assert 1 in {1}
    assert 3 in {1, 2, 3}
    assert 4 not in {1, 2, 3}

def add():
    # add/insert element in set
    s = {2, 3, 1}
    s.add(4)
    assert s == {1, 2, 3, 4}

    # no-op if element already exists
    s.add(4)
    assert s == {1, 2, 3, 4}

def comprehension():
    c = {x for x in [1, 1, 2, 3] if x % 2}
    assert c == {1, 3}

def update():
    # combine two sets
    # note: '+' operator does not work for sets
    a = {1, 2, 3}
    b = {2, 3, 4}
    a.update(b)
    assert a == {1, 2, 3, 4}

def union():
    # like update but returns new set
    a = {1, 2, 3}
    b = {2, 3, 4}
    u = a.union(b)
    assert a == {1, 2, 3}
    assert b == {2, 3, 4}
    assert u == {1, 2, 3, 4}

def remove():
    s = {'a', 'b', 'c'}
    s.remove('b')
    assert s == {'a', 'c'}

    # throws KeyError. Use 'in' first.
    # s.remove('fake_elem')
    if 'fake_elem' in s:
        s.remove('fake_elem')

    # use discard() to avoid conditionals and exceptions
    s.discard('fake_elem')

def discard():
    # similar to remove, but does not throw errors
    s = {'a', 'b', 'c'}
    s.discard('a')
    s.discard('fake_elem') # no-op when element doesn't exist
    assert s == {'b', 'c'}

def clear():
    s = {1, 2}
    s.clear()
    assert len(s) == 0

def deepCopy():
    a = {2, 4, 6}
    b = a.copy()
    b.add(5)
    assert a == {2, 4, 6}
    assert b == {2, 4, 5, 6}

def frozenSet():
    f = frozenset((2, 1, 2, 3))
    assert f == frozenset({1, 2, 3})

    # converts dictionary keys to frozenset
    person = {'name': 'John',
              'age': 99,
              'zip': 60202}
    f = frozenset(person)
    assert f == {'name', 'age', 'zip'}

def sequence():
    # Generate sequence of 1 to 100
    listSeq = list(range(1, 101))
    setSeq = {*listSeq}
    assert sum(setSeq) == (100 * 101) / 2 # 5050

def pop():
    # pop() removes a 'random' element from the set
    s = {4, 3, 2, 1}
    elem = s.pop()
    assert elem == 1
    elem = s.pop()
    assert elem == 2
    elem = s.pop()
    assert elem == 3
    elem = s.pop()
    assert elem == 4

    assert len(s) == 0

# set difference (setdiff)
def difference():
    s = {1, 2, 3}
    t = {2, 3, 4}

    diff = s.difference(t)
    assert diff == {1} # 1 is in 's' but not 't'

    diff = t.difference(s)
    assert diff == {4} # 4 is in 't' but not 's

    diff = s.difference(s)
    assert diff == set() # set difference with self produces empty set

    # set also supports the subtraction (-) operator
    diff = s - t
    assert diff == {1}

def main():
    empty()
    create()
    find()
    add()
    comprehension()
    update()
    union()
    remove()
    discard()
    clear()
    deepCopy()
    frozenSet()
    sequence()
    pop()
    difference()

if __name__ == '__main__':
    main()
    print('Tests passed!')
