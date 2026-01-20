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

    # method
    u = a.union(b)
    assert a == {1, 2, 3}
    assert b == {2, 3, 4}
    assert u == {1, 2, 3, 4}

    # '|' operator
    u = a | b
    assert u == {1, 2, 3, 4}

    # in-place union (|=)
    a |= b
    assert a == {1, 2, 3, 4}

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

def disjoint():
    s1 = {1, 2, 3}
    s2 = {4, 5}
    # s1 and s2 have no elements in common
    assert s1.isdisjoint(s2)
    assert not s1.isdisjoint(s1)

def subset():
    s1 = {1, 2, 3}
    s2 = {1, 2, 3, 4, 5}

    # s1 is a subset of s2 because all elements of s1 are in s2
    assert s1.issubset(s2)
    assert s1.issubset(s1)

    # '<=' is equivalent syntax
    assert s1 <= s2

    # reverse is not true
    assert not s2.issubset(s1)

def superset():
    s1 = {1, 2, 3}
    s2 = {1, 2, 3, 4, 5}

    assert s2.issuperset(s1)
    assert s2 >= s1 # equivalent syntax

    assert not s1.issuperset(s2)

def intersection():
    # create 2 sets containing '1' and '3'
    a = {1, 2, 3}
    b = {1, 3, 4}

    # method
    i = a.intersection(b)
    assert i == {1, 3}

    # '&' operator
    i = a & b
    assert i == {1, 3}

    # in-place intersection (&=)
    a &= b
    assert a == {1, 3}

def symmetric_difference():
    a = {1, 2, 3}
    b = {3, 2, 5}

    # method
    x = a.symmetric_difference(b)
    # 1 is in a but not b
    # 5 is in b but not a
    assert x == {1, 5}

    # '^' operator for symmetric difference (xor)
    x = a ^ b
    assert x == {1, 5}

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
    disjoint()
    subset()
    superset()
    intersection()
    symmetric_difference()

if __name__ == '__main__':
    main()
    print('Tests passed!')
